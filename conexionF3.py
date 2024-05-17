import mysql.connector
from mysql.connector import Error
import csv
import re

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



# Función para extraer el nombre de la provincia
def extraer_provincia(texto):
    # Buscar el patrón "Embalses de [provincia]" y extraer solo el nombre de la provincia
    match = re.search(r'Embalses de (.*)$', texto)
    if match:
        match2 = re.search(r'la .* de (.*)$',match.group(1))
        if match2:
            return match2.group(1)
        else:
            return match.group(1)
    else:
        return None

def extraer_embalse(texto):
    # Buscar el patrón "Embalses de [provincia]" y extraer solo el nombre de la provincia
    match = re.search(r'Embalse de (.*)$', texto)
    if match:
        return match.group(1)
    else:
        return texto

if __name__ == '__main__':
    usr = input("User: \t")
    pwd = input("Password: \t")
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f3",
        26142)
    

    cursor = connection.cursor()


    # Abrir el archivo CSV y leer los datos
    with open('embalsesProvincia.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Si hay encabezados, omítelos
        for row in csv_reader:
            # Expresion regular para obtener la provincia
            prov = extraer_provincia(row[0])

            emb = extraer_embalse(row[2])
            try:
                cursor.execute('''INSERT INTO ambitoEmbalse (provincia, nombreEmbalse)
                            VALUES (%s, %s)''', (prov, emb))
                connection.commit()  # Commit the transaction
            except Exception as e:
                print("Error occurred:", e)
                connection.rollback()  # Rollback the transaction in case of error

    connection.close()
