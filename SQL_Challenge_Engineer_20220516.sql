-- Queries Challenge_Engineer (XalDigital). 

-- 1.- ¿Cuál es el nombre del aeropuerto que ha tenido mayor movimiento durante el año?

SELECT v.Anio, ap.NOMBRE_AEROPUERTO as Aeropuerto, v.Movimientos 
FROM (
		SELECT YEAR(DIA) as 'Anio', ID_AEROPUERTO, count(*) AS 'movimientos'
		FROM Vuelos
		GROUP BY YEAR(DIA), ID_AEROPUERTO
		) AS v
	JOIN (
			SELECT MAX(v.movimientos) AS 'max_mov'
			FROM (
					SELECT ID_AEROPUERTO, count(*) AS 'movimientos'
					FROM Vuelos
					GROUP BY ID_AEROPUERTO
					) AS v
		) AS vmax on vmax.max_mov = v.movimientos
LEFT JOIN Aeropuertos AS ap on ap.ID_AEROPUERTO = v.ID_AEROPUERTO
WHERE Anio = (SELECT MAX(YEAR(DIA)) FROM Vuelos);

-- 2.- ¿Cuál es el nombre de la aerolínea que ha realizado mayor número de vuelos durante el año?

SELECT v.Anio, ar.NOMBRE_AEROLINEA as 'Aerolinea', v.Movimientos 
FROM (
		SELECT YEAR(DIA) as 'Anio', ID_AEROLINEA, count(*) AS 'movimientos'
		FROM Vuelos
		GROUP BY ID_AEROLINEA, YEAR(DIA)
		) AS v
	JOIN (
			SELECT MAX(v.movimientos) AS 'max_mov'
			FROM (
					SELECT ID_AEROLINEA, count(*) AS 'movimientos'
					FROM Vuelos
					GROUP BY ID_AEROLINEA
					) AS v
		) AS vmax on vmax.max_mov = v.movimientos
LEFT JOIN Aerolineas AS ar on ar.ID_AEROLINEA = v.ID_AEROLINEA
WHERE v.Anio = (SELECT MAX(YEAR(DIA)) FROM Vuelos);

-- 3.- ¿En qué día se han tenido mayor número de vuelos?
SELECT  v.DIA as 'Dia', v.Movimientos
FROM (
		SELECT DIA, count(*) AS 'movimientos'
		FROM Vuelos
		GROUP BY DIA
		) AS v
	JOIN (
			SELECT MAX(v.movimientos) AS 'max_mov'
			FROM (
					SELECT DIA, count(*) AS 'movimientos'
					FROM Vuelos
					GROUP BY DIA
					) AS v
		) AS vmax on vmax.max_mov = v.movimientos

-- 4.- ¿Cuáles son las aerolíneas que tienen más de 2 vuelos por día? 

SELECT ar.NOMBRE_AEROLINEA as 'Aerolinea'
		,COUNT(*) as 'Num_Vuelos'
FROM Vuelos as v
LEFT JOIN Aerolineas as ar ON ar.ID_AEROLINEA = v.ID_AEROLINEA
GROUP BY ar.NOMBRE_AEROLINEA
HAVING COUNT(*) > 2 