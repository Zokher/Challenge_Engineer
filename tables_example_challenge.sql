USE [Test]
GO

DROP TABLE IF EXISTS [Aerolineas]
CREATE TABLE [Aerolineas](
	[ID_AEROLINEA] [int] NOT NULL,
	[NOMBRE_AEROLINEA] [varchar](20) NULL
) ON [PRIMARY]
GO

INSERT INTO [Aerolineas] VALUES (1,'Volaris');
INSERT INTO [Aerolineas] VALUES (2,'Aeromar');
INSERT INTO [Aerolineas] VALUES (3,'Interjet');
INSERT INTO [Aerolineas] VALUES (4,'Aeromexico');

DROP TABLE IF EXISTS [Aeropuertos]
CREATE TABLE [Aeropuertos](
	[ID_AEROPUERTO] [int] NULL,
	[NOMBRE_AEROPUERTO] [varchar](20) NULL
) ON [PRIMARY]
GO

INSERT INTO [Aeropuertos] VALUES (1,'Benito Juarez');
INSERT INTO [Aeropuertos] VALUES (2,'Guanajuato');
INSERT INTO [Aeropuertos] VALUES (3,'La paz');
INSERT INTO [Aeropuertos] VALUES (4,'Oaxaca');


DROP TABLE IF EXISTS [Movimientos]
CREATE TABLE [Movimientos](
	[ID_MOVIMIENTO] [int] NULL,
	[DESCRIPCION] [varchar](20) NULL
) ON [PRIMARY]
GO

INSERT INTO [Movimientos] VALUES (1,'Salida');
INSERT INTO [Movimientos] VALUES (2,'Llegada');

DROP TABLE IF EXISTS [Vuelos]
CREATE TABLE [Vuelos](
	[ID_AEROLINEA] [int] NOT NULL,
	[ID_AEROPUERTO] [int] NOT NULL,
	[ID_MOVIMIENTO] [int] NOT NULL,
	[DIA] [date] NULL
) ON [PRIMARY]
GO

INSERT INTO [Vuelos] VALUES (1,1,1,'2021-05-02');
INSERT INTO [Vuelos] VALUES (2,1,1,'2021-05-02');
INSERT INTO [Vuelos] VALUES (3,2,2,'2021-05-02');
INSERT INTO [Vuelos] VALUES (4,3,2,'2021-05-02');
INSERT INTO [Vuelos] VALUES (1,3,2,'2021-05-02');
INSERT INTO [Vuelos] VALUES (2,1,1,'2021-05-02');
INSERT INTO [Vuelos] VALUES (2,3,1,'2021-05-04');
INSERT INTO [Vuelos] VALUES (3,4,1,'2021-05-04');
INSERT INTO [Vuelos] VALUES (3,4,1,'2021-05-04');



