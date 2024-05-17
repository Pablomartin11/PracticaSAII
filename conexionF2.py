import mysql.connector
from mysql.connector import Error


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

    usr = input("User: \t")
    pwd = input("Password: \t")
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f2",
        26142)
    

    cursor = connection.cursor()
    
    

    # Abrir el archivo en modo lectura
    with open('DatosEmbalsesResum.txt', 'r',encoding='iso-8859-1') as archivo:
        # Leer todas las líneas del archivo
        lineas = archivo.readlines()

    datos=[]

    for linea in lineas:
        # Separar la línea por punto y coma
        valores = linea.strip().split(';')
        # Agregar los valores a la lista de datos
        datos.append(valores)



    for fila in datos:
        embalse_nombre=fila[1]
        fecha=fila[2]
        agua_total = float(fila[3].replace(',', '.').strip('"'))
        agua_actual= float(fila[4].replace(',', '.').strip('"'))

        try:
            cursor.execute('''INSERT INTO datosEmbalse (embalse_nombre, fecha, agua_total, agua_actual)
                            VALUES (%s, %s, %s, %s)''', (embalse_nombre,fecha,agua_total,agua_actual))
            connection.commit()  # Commit the transaction
        except Exception as e:
            print("Error occurred:", e)
            connection.rollback()  # Rollback the transaction in case of error

        


    connection.commit()
    connection.close()
        




