from SPARQLWrapper import SPARQLWrapper, JSON, CSV
import csv
import mysql.connector
from mysql.connector import Error


def conexion_sparql():
    
    endpoint_url = "http://datos.gob.es/virtuoso/sparql" 

    # Crear un objeto SPARQLWrapper para el punto SPARQL
    sparql = SPARQLWrapper(endpoint_url)

    # Escribir tu consulta SPARQL
    query = """
        select distinct ?dataset ?url where {
        ?dataset a <http://www.w3.org/ns/dcat#Dataset> .
        ?dataset <http://purl.org/dc/terms/title> "Climatología en Asturias: temperaturas, precipitaciones y horas de sol"@es .
        ?dataset <http://www.w3.org/ns/dcat#distribution> ?distribution .
        ?distribution <http://www.w3.org/ns/dcat#accessURL> ?url .
        }
    """

    # Establecer la consulta SPARQL en el objeto SPARQLWrapper
    sparql.setQuery(query)

    # Los resultados deben ser devueltos en formato JSON
    sparql.setReturnFormat(JSON)

    try:
        # Realizar la consulta SPARQL
        results = sparql.query().convert()
        return results

    except Exception as e:
        print(f"Error occurred: {e}")


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




if __name__ == '__main__':
    print("\nDatos f4 - Climatología Asturias 2020-2023 - Punto SparQl")
    results = conexion_sparql()
    # Iterar sobre los resultados e imprimirlos
    for result in results["results"]["bindings"]:
        print("URL - sitio en datosgob.es:  ",result["dataset"]["value"])
        print("URL - dataset obtenido:  ",result["url"]["value"])


    usr = input("User: \t")
    pwd = input("Password: \t")
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f4",
        26142)

    cursor = connection.cursor()
    
    # Abrir el archivo CSV y leer los datos
    with open('f4.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            fecha = row[0]
            estacion = row[1]
            tmed = row[2]
            tmed_max = row[3]
            tmed_min = row[4]
            precip = row[5]
            try:
                cursor.execute('''INSERT INTO temperaturaAsturias (fecha, estacionClimatologica, tmed,tmed_max, tmed_min, precip)
                            VALUES (%s, %s, %s, %s, %s, %s)''', (fecha, estacion, tmed, tmed_max, tmed_min, precip))
                connection.commit()  # Commit the transaction
            except Exception as e:
                print("Error occurred:", e)
                connection.rollback()


            
    # Guardar los cambios y cerrar la conexión
    connection.commit()
    connection.close()
