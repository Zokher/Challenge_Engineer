import requests
import pandas as pd

pd.set_option('display.max_columns', None)

if __name__ == '__main__':
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    response = requests.get(url)

    if response.status_code == 200:
        print('                                                                                     ')
        print('*********************************** ACTIVIDAD 1 ***********************************')
        print('                                                                                     ')
        print('Conectarse al enlace')
        print('                                                                                     ')
        print('Response:', response, '**Conexión exitosa, comienza consulta del json....')
        data = response.json()


        #Definición de variables para almacenamiento de consulta
        answer_count = []
        creation_date = []
        #link = []
        is_answered = []
        view_count = []
        reputation = []
        display_name = []
        question_id = []

        #Extracción de información del JSON
        for item in data['items']:
            answer_count.append(item['answer_count'])
            creation_date.append(item['creation_date'])
            #link.append(item['link'])
            is_answered.append(item['is_answered'])
            view_count.append(item['view_count'])
            reputation.append(item['owner']['reputation'])
            display_name.append(item['owner']['display_name'])
            question_id.append(item['question_id'])


        #Diccionario de paso
        dict = {
            'Numero_respuestas': answer_count,
            'Fecha_de_creacion': creation_date,
            #'Liga': link,
            'Respuesta_contestada': is_answered,
            'Visitas': view_count,
            'Reputacion': reputation,
            'Nombre_a_mostrar': display_name,
            'Id_Pregunta': question_id
        }

        #Conversión a df
        questions_df = pd.DataFrame(dict, columns=['Id_Pregunta',
                                              'Nombre_a_mostrar',
                                              'Fecha_de_creacion',
                                              'Reputacion',
                                              'Respuesta_contestada',
                                              'Numero_respuestas',
                                              'Visitas'
                                              ])

        print('                                                                                     ')
        print('*********************************** ACTIVIDAD 2 ***********************************')
        print('                                                                                     ')
        print('Obtener el número de respuestas contestadas y no contestadas')
        print('                                                                                     ')

        actividad_2 = questions_df['Respuesta_contestada'].value_counts().reset_index()
        actividad_2.columns = ['Pregunta_contestada','#Preguntas']
        print(actividad_2)



        print('                                                                                     ')
        print('*********************************** ACTIVIDAD 3 ***********************************')
        print('                                                                                     ')
        print('Obtener la respuesta con menor número de vistas')
        print('                                                                                     ')

        actividad_3_vis_min = questions_df['Visitas'].min()
        actividad_3_id = questions_df[questions_df['Visitas'] == actividad_3_vis_min]['Id_Pregunta']
        actividad_3_name = questions_df[questions_df['Visitas'] == actividad_3_vis_min]['Nombre_a_mostrar']
        actividad_3_vis_min = questions_df[questions_df['Visitas'] == actividad_3_vis_min]['Visitas']
        print('La pregunta ', str(actividad_3_id.values[0]), ' tiene ', str(actividad_3_vis_min.values[0]), ' visitas y pertenece a ', str(actividad_3_name.values[0]))



        print('                                                                                     ')
        print('*********************************** ACTIVIDAD 4 ***********************************')
        print('                                                                                     ')
        print('Obtener la respuesta más vieja y más actual')
        print('                                                                                     ')

        #Fecha de segundos a tiempo dias y hrs
        questions_df['Fecha_de_creacion_fix'] = questions_df['Fecha_de_creacion'].astype('timedelta64[s]')
        questions_df['Fecha_de_creacion_fix'] = questions_df['Fecha_de_creacion_fix'].astype(str)

        actividad_4_newest = questions_df['Fecha_de_creacion'].min()
        actividad_4_id = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_newest]['Id_Pregunta']
        actividad_4_name = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_newest]['Nombre_a_mostrar']
        actividad_4_newest = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_newest]['Fecha_de_creacion_fix']
        print('La pregunta más nueva se creó hace ', actividad_4_newest.values[0],' tiene el id ', str(actividad_4_id.values[0]),' y pertenece a ', str(actividad_4_name.values[0]))

        actividad_4_oldest = questions_df['Fecha_de_creacion'].max()
        actividad_4_id = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_oldest]['Id_Pregunta']
        actividad_4_name = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_oldest]['Nombre_a_mostrar']
        actividad_4_oldest = questions_df[questions_df['Fecha_de_creacion'] == actividad_4_oldest]['Fecha_de_creacion_fix']
        print('La pregunta más vieja se creó hace ', actividad_4_oldest.values[0], ' tiene el id ',str(actividad_4_id.values[0]), ' y pertenece a ', str(actividad_4_name.values[0]))



        print('                                                                                     ')
        print('*********************************** ACTIVIDAD 5 ***********************************')
        print('                                                                                     ')
        print('Obtener la respuesta del owner que tenga mayor reputación')
        print('                                                                                     ')

        actividad_5_rep = questions_df['Reputacion'].max()
        actividad_5_id = questions_df[questions_df['Reputacion'] == actividad_5_rep]['Id_Pregunta']
        actividad_5_name = questions_df[questions_df['Reputacion'] == actividad_5_rep]['Nombre_a_mostrar']
        actividad_5_rep = questions_df[questions_df['Reputacion'] == actividad_5_rep]['Reputacion']
        print('La pregunta con el id ', actividad_5_id.values[0], ' pertenece a ', str(actividad_5_name.values[0]), ' y tiene una reputación de ', str(actividad_5_rep.values[0]))


        print('                                                                                     ')
        print('                                                                                     ')
        print('                                                                                     ')
