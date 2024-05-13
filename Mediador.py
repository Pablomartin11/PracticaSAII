import mysql.connector
from mysql.connector import Error
from datetime import datetime

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
    connection1 = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f1",
        26142)
    
    connection2 = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f2",
        26142)
    
    connection3 = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "f3",
        26142)
    
    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        usr,
        pwd,
        "mediador",
        26142)
    

    cursor1 = connection1.cursor()
    
    cursor2 = connection2.cursor()
    
    cursor3 = connection3.cursor()

    cursor = connection.cursor()


    #EmbalsesAst
    cursor1.execute("SELECT fecha, nombre, provincia, np_010, n_nie, evap FROM climatologiaAsturias")
    datos_f1 = cursor1.fetchall()

    cursor2.execute("SELECT embalse_nombre, fecha, agua_total, agua_actual FROM datosEmbalse")
    datos_f2 = cursor2.fetchall()

    cursor3.execute("SELECT provincia, nombreEmbalse FROM ambitoEmbalse")
    datos_f3 = cursor3.fetchall()

    

    for fila2 in datos_f2:
        embalse_nombre, fecha1, aguaTotal, aguaActual = fila2
        embalse_nombre= embalse_nombre.replace('"', '')

        for fila3 in datos_f3:
            provincia2, nombreEmbalse = fila3   
            
            if (embalse_nombre == nombreEmbalse):

                for fila1 in datos_f1:
                    fecha, nombre, provincia, np010, nNie, evap = fila1

                    # Convertir fecha2_str al formato "2020-01"
                    fecha2 = datetime.strptime(fecha1.strip('"'), "%d/%m/%Y").strftime("%Y-%m")

                    año, mes = fecha.split('-')
                    if(len(mes))==1:
                        mes = '0'+mes
                    
                    fecha= f"{año}-{mes}"

                    if (provincia==provincia2 and fecha2 == fecha):
                        sql = "INSERT INTO embalsesAst (fecha, nombre, nombreEmbalse, provincia,agua_total, agua_actual, np_010, n_nie, evap) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (fecha, nombre,nombreEmbalse, provincia,aguaTotal, aguaActual, np010, nNie, evap)
                        try:
                            cursor.execute(sql, val)
                            connection.commit()  # Commit the transaction
                        except Exception as e:
                            print("Error occurred:", e)
                            connection.rollback()  # Rollback the transaction in case of error

                
                



    
    