import mysql.connector
from mysql.connector import Error
import requests

def conectar_a_mysql(host_name, user_name, user_password, db_name,port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port = port
        )
        print("Conexión a MySQL DB exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")

    return connection

# Ejemplo de uso
if __name__ == '__main__':
    usr = input("User: \t")
    pwd = input("Password: \t")
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "s1",
        26122)
    
    cursor = connection.cursor()


    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/2020/aniofin/2020/estacion/1212E"

    querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwYWJsb21kYjExQGdtYWlsLmNvbSIsImp0aSI6IjJkYmViZDA2LTlmMDQtNGZmMS1hYTE5LWM2MWFhZjcxMWYxMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzEzODA1NTYyLCJ1c2VySWQiOiIyZGJlYmQwNi05ZjA0LTRmZjEtYWExOS1jNjFhYWY3MTFmMTMiLCJyb2xlIjoiIn0.2-snjCrzkC95euVJcVDMSm-0tJe4A2mItm5vecCRYlE"}

    headers = {
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()

    if response['estado'] == 200:
        url_datos = response['datos']

        response_datos = requests.get(url_datos)
        datos_api = response_datos.json()

        for dato in datos_api:
            fecha = dato['fecha']
            indicativo = dato['indicativo']
            tm_mes = dato['tm_mes']
            tm_max = dato['tm_max']
            tm_min = dato['tm_min']
            p_mes = dato['p_mes']
            p_max = dato['p_max']
            np_010 = dato['np_010']
            n_nie = dato['n_nie']
            if 'evap' in dato:
                evap = dato['evap']
            else: 
                evap = None
            
            sql = "INSERT INTO f1.climatologiaAsturias VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
            val = (fecha, indicativo, tm_mes, tm_max,tm_min,p_mes,p_max,np_010,n_nie,evap)
            cursor.execute(sql, val)


    cursor.close()

    if connection:
        connection.close()

    
    