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

# Ejemplo de uso
if __name__ == '__main__':
    usr = input("User: \t")
    pwd = input("Password: \t")
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "ClimaCYL",
        26122)
    
    cursor = connection.cursor()

    query = ("SELECT * FROM Clima")
    cursor.execute(query)
    
    for item in cursor:
        print(item)
    cursor.close()

    if connection:
        connection.close()

    
    
