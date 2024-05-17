import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter.font import Font

# Datos de ejemplo para las consultas
data1 = {'Fecha': ['2023-05-01', '2023-06-01', '2023-07-01'], 'Zona': ['Norte', 'Centro', 'Sur'], 'Temperatura Media': [16, 17, 18]}
data2 = {'Fecha': ['2023-05-02', '2023-06-02', '2023-07-02'], 'Zona': ['Norte', 'Centro', 'Sur'], 'Precipitaciones': [8, 9, 10]}
data3 = {'Fecha': ['2023-05-03', '2023-06-03', '2023-07-03'], 'Embalse': ['Embalse1', 'Embalse2', 'Embalse3'], 'Agua': [25, 30, 35]}

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

# Funciones para mostrar los datos en la tabla
def llenar_tabla(tabla, datos, colnames):
    tabla.delete(*tabla.get_children())
    

    tabla["columns"] = colnames
    for columna in colnames:
        tabla.heading(columna, text=columna)

    for fila in datos:
        tabla.insert("", "end", values=fila)

    # Ajustar el ancho de las columnas según el contenido
    j = 0
    for columna in tabla["columns"]:
        tabla.column(columna, width=Font().measure(columna), anchor="center")
        
        for i in range(0,len(datos)):
            if(datos[i][j]!=None):
                width = Font().measure(datos[i][j])
                if tabla.column(columna, width=None) < width:
                    tabla.column(columna, width=width)
        
        j = j +1

def consulta1(entry,tabla, cursor):
    print("Botón 1 clicado")
    try:
        temp = int(entry.get())
        if temp < 0:
            raise ValueError("El valor debe ser un entero positivo.")
        else:
            sql = "SELECT fecha, nombre, tmed FROM temperaturaAst WHERE tmed > "+str(temp)
            cursor.execute(sql)
            tuplas = cursor.fetchall()
            datos=[]

            for tupla in tuplas:
                # transformar de tupla  y Agregarla los valores a la lista de datos
                datos.append(list(tupla))
            colnames = ("Fecha", "Ubicación Estación Climatologica", "Temperatura Media")
            llenar_tabla(tabla, datos, colnames)
            entry.config(bg='white')
    except ValueError as e:
        entry.config(bg='red')
        tk.messagebox.showerror("Entrada no válida", "Por favor, introduce un número entero válido.")



    
    

def consulta2(entry,tabla, cursor):
    print("Botón 2 clicado")
    try:
        temp = int(entry.get())
        if temp < 0:
            raise ValueError("El valor debe ser un entero positivo.")
        else:
            cursor.execute("SELECT fecha, nombre, precip FROM precipitacionesAst WHERE precip >"+str(temp))
            tuplas = cursor.fetchall()
            datos=[]

            for tupla in tuplas:
                # transformar de tupla  y Agregarla los valores a la lista de datos
                datos.append(list(tupla))
            colnames = ("Fecha", "Ubicación Estación Climatologica", "Precipitaciones (mm)")
            llenar_tabla(tabla, datos, colnames)
            entry.config(bg='white')

    except ValueError as e:
        entry.config(bg='red')
        tk.messagebox.showerror("Entrada no válida", "Por favor, introduce un número entero válido.")




    

def consulta3(entry1,entry2,tabla, cursor):
    print("Botón 3 clicado")
    # Meter consulta 3
    try:
        days = int(entry1.get())
        acum = int(entry2.get())
        if days < 0 or acum < 0:
            raise ValueError("Los valores deben ser enteros positivos.")
        else:
            cursor.execute("SELECT P.fecha, E.nombreEmbalse, E.agua_actual FROM precipitacionesAst P, embalsesAst E WHERE np_010 >"+str(days)+" and precip > "+str(acum)+" and E.fecha = P.fecha and E.nombre = P.nombre")
            tuplas = cursor.fetchall()
            datos=[]
            for tupla in tuplas:
                # transformar de tupla  y Agregarla los valores a la lista de datos
                datos.append(list(tupla))
            colnames = ("Fecha", "Nombre Embalse", "Agua actual del embalse")
            llenar_tabla(tabla, datos, colnames)
            entry1.config(bg='white')
            entry2.config(bg='white')
    except ValueError as e:
        entry1.config(bg='red')
        entry2.config(bg='red')
        tk.messagebox.showerror("Entrada no válida", "Por favor, introduce un número entero válido.")




    


# Función para crear una sección de consulta
def create_consulta_section(frame, description1, default_value, description2, tabla, cursor,consulta,is_double=False):
    section_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE)
    section_frame.pack(fill=tk.X, padx=5, pady=5)

    # Crear un Text widget para la descripción
    text_widget = tk.Text(section_frame, height=3, wrap=tk.WORD, font=("Arial", 10))
    text_widget.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

    # Insertar el texto antes del campo de entrada
    text_widget.insert(tk.END, description1)

    # Crear campos de entrada y añadirlos al Text widget
    if is_double:
        entry_days = tk.Entry(section_frame, width=5)
        entry_days.insert(0, default_value.split(' y ')[0])
        text_widget.window_create(tk.END, window=entry_days)
        text_widget.insert(tk.END, " dias y un acumulado mayor de ")
        entry_acum = tk.Entry(section_frame, width=5)
        entry_acum.insert(0, default_value.split(' y ')[0])
        text_widget.window_create(tk.END, window=entry_acum)
    else:
        entry_window = tk.Entry(section_frame, width=5)
        entry_window.insert(0, default_value)
        text_widget.window_create(tk.END, window=entry_window)

    # Botón para ejecutar la consulta
    if is_double:
        tk.Button(section_frame, text="Mostrar datos", command=lambda: consulta(entry_days, entry_acum,tabla,cursor)).pack(side=tk.RIGHT, padx=5, pady=5)
    else:
        tk.Button(section_frame, text="Mostrar datos", command=lambda: consulta(entry_window,tabla,cursor)).pack(side=tk.RIGHT, padx=5, pady=5)



if __name__=='__main__':

    connection = conectar_a_mysql(
        "virtual.lab.inf.uva.es",
        "alex",
        "alonso33",
        "mediador",
        26142)
    cursor = connection.cursor()

    # Crear la ventana principal
    root = tk.Tk()
    root.title('Intefaz gráfica del Mediador')
    root.geometry("800x600")  # Establecer tamaño inicial

    # Crear el frame principal
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)


    # Crear el frame para la tabla
    table_frame = tk.Frame(root)
    table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    


    # Creacion de la tabla 
    tabla = ttk.Treeview(table_frame)
    tabla["show"] = "headings"  # Ocultar la columna del índice
    tabla.pack(fill="both", expand=True)

    # Crear las secciones de consulta
    create_consulta_section(main_frame, " 1.- Fecha en las que la temperatura media supera los ", "15", " ºC en las diferentes zonas de Asturias.", tabla, cursor ,consulta1)
    create_consulta_section(main_frame, " 2.- Fechas y zonas en las que las precipitaciones son abundantes. Mayores de ", "7", " mm).", tabla, cursor ,consulta2)
    create_consulta_section(main_frame, " 3.- Fecha, nombre y agua de los embalses en los meses que llovió más de ", "9", " mm.", tabla, cursor,consulta3,is_double=True )

    

    # Ejecutar la aplicación
    root.mainloop()
