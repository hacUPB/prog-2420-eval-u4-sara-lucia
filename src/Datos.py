import csv 
import matplotlib.pyplot as plt 
import os 
import numpy as np

# Funciones archivos de texto(.txt)

#Función contar palabras
def cont_palabras(archivo_txt): 
    try:
        with open(archivo_txt, 'r') as archivo:
            leer = archivo.readlines()
            texto = ''.join(leer)
            palabras = texto.split()
            print(f"El número de palabras es: {len(palabras)}")
    except FileNotFoundError: 
            print("Archivo no encontrado. Verifique e intente nuevamente")

#Función reemplazar una palabra por otra
def reemp_palabras(archivo_txt): 
    palabra_1 = str(input("Ingrese la palabra que quiere reemplazar: "))
    palabra_2 = str(input("Ingrese la palabra que quiere colocar: "))
    try: 
        with open(archivo_txt, 'r+') as archivo: 
            leer = archivo.read()
            palabra_nueva = leer.replace(palabra_1, palabra_2) 
            archivo.seek(0)
            archivo.write(palabra_nueva)
            archivo.truncate()
            print(f"Palabra reemplazada correctamente")
    except FileNotFoundError: 
     print("Archivo no encontrado. Verifique e intente nuevamente")

#Función contar número de caracteres
def num_caracteres(archivo_txt):
    try:
        with open(archivo_txt, 'r') as archivo:
            texto = archivo.read()
            caracteres_espacio = len(texto)
            caracteres_sin_espacio = len(texto.replace(' ', ''))
            print(f"Numero de caracteres con espacios: {caracteres_espacio}")
            print(f"Número de caracteres sin espacios: {caracteres_sin_espacio}")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique e intente nuevamente")

#Función submenú 
def menu_arch_txt():
    while True: 
        opcion_texto = (input("Seleccione el número de la opción que desea realizar. \n1. Contar número de palabras \n2. Reemplazar una palabra por otra \n3. Contar numero de caracteres \n4. Menú principal")).strip()
        archivo_txt = input("Ingrese la ruta del archivo: ").strip('"').strip("'")
        if opcion_texto == "1": 
            cont_palabras(archivo_txt)
        elif opcion_texto == "2":
            reemp_palabras(archivo_txt)
        elif opcion_texto == "3":
            num_caracteres(archivo_txt)
        elif opcion_texto == "4":
            print("Regresando al menú principal")
            break 
        else: 
            print("Opción inválida. Seleccione una correcta")
        

#Funciones archivos separados por comas(.csv)

#Función mostrar 15 primeras filas 
def leer_filas(archivo_csv):
    try: 
        with open(archivo_csv, 'r') as csvfile: 
            lector = csv.reader(csvfile)
            contador = 0
            for fila in lector:
                if contador < 15: 
                    print (fila)
                    contador += 1
                else: 
                    break 
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique e intente nuevamente")

#Función calcular estadísticas
def cal_est(archivo_csv):
    columna = input("Ingrese la columna que quiere usar ").strip()
    info =[]
    try: 
        with open(archivo_csv, 'r') as csvfile: 
            lector = csv.reader(csvfile)
            encabezados = next(lector)

            #Encontrar columna 
            if columna in encabezados: 
                print("Columna encontrada")
                indice_columna = encabezados.index(columna)
                for fila in lector: 
                    try: 
                        valor = float(fila[indice_columna])
                        info. append(valor)
                    except ValueError:
                        print("El valor de la fila no es un número")
            else:  
                print("Ingrese una columna válida") 
                return

            #Calcular estadísticas
            if info: 
                numero_datos = len(info)
                promedio = sum(info)/numero_datos
                info_ordenada = sorted(info)
                mediana = info_ordenada[numero_datos // 2] if numero_datos % 2 == 1 else (info_ordenada[numero_datos //2 - 1] + info_ordenada [numero_datos // 2 ] /2)
                valor_max = max(info)
                valor_min = min(info)
                print(f"Promedio: {promedio}")
                print(f"Mediana: {mediana}")
                print(f"Valor máximo: {valor_max}")
                print(f"Valor mínimo: {valor_min}")
            else: 
                print("No se encontraron datos para hacer el cálculo")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique e intente nuevamente")

#Función grafica
def grafica(archivo_csv):
    try: 
     columna = input("Ingrese la columna que desea graficar: ")
     info = []
     with open(archivo_csv, 'r') as csvfile: 
            lector = csv.reader(csvfile)
            encabezados = next(lector)
            if columna in encabezados: 
                print("Columna encontrada")
                indice_columna = encabezados.index(columna)
                
                for fila in lector: 
                    try:
                        valor = float(fila[indice_columna])
                        info.append(valor)
                    except ValueError:
                        print (f"El valor '{fila[indice_columna]}' de la fila no es un número y será ignorado")
                        
                columna_x = input("Ingrese el nombre para el eje x:")
                columna_y = input("Ingrese el nombre del eje y: ")         
                        
                if info: 
                    plt.plot(info)
                    plt.title(f"Gráfica de la columna '{columna}' ")
                    plt.xlabel(columna_x)
                    plt.ylabel(columna_y)
                    plt. show()
                else:
                            print ("No hay datos numéricos para graficar la columna ")
            else: 
                print("Columna no encontrada. Verifique e intente nuevamente")
    except FileNotFoundError: 
     print("Archivo no encontrado. Verifique e intente nuevamente")

#Función submenú 
def men_arch_csv():
    while True: 
        opcion_csv = input("Seleccione el número de la opción que desea realizar. \n1. Mostrar 15 primeras filas \n2. Calcular estadísiticas \n3. Graficar columna  \n4. Menú principal").strip()
        if opcion_csv != 4:
            archivo_csv = input("Ingrese la ruta del archivo").strip('"').strip("'")
            if opcion_csv == '1':
                leer_filas(archivo_csv)
            elif opcion_csv == '2':
                cal_est(archivo_csv)
            elif opcion_csv == '3':
                grafica(archivo_csv)
        else: 
            print("Regresando al menú principal")
            break

#Funciones archivos

#Función listar archivos 
def listar():
    ruta_actual = os.getcwd()
    print(f"Archivos de la rutal actual: {ruta_actual}")
    archivos = os.listdir(ruta_actual)
    for archivo in archivos:
        if os.path.isfile(os.path.join(ruta_actual, archivo)):
            print(archivo)

#Función ingresar ruta donde listar archivos 
def ruta_listar():
    ruta = input("Ingrese la ruta que desea listar: "). strip('"').strip("'")
    if os.path.isdir (ruta):
        print (f"Archivos en el directorio ({ruta})")
        for archivo in os.listdir(ruta):
            if os.path.isfile(os.path.join(ruta,archivo)):
                print(archivo)
    else: 
        print("La ruta ingresada es inválida o no existe")

#Función submenú 
def men_arch():
    while True: 
        opcion_arch = input("Seleccione el número de la opción que desea realizar. \n1. Listar archivos en la ruta actual  \n2. Ingresar una ruta donde listar archivos \n3. Menú principal")
        if opcion_arch == '1':
            listar()
        elif opcion_arch == '2':
            ruta_listar()
        elif opcion_arch == '3':
            print("Regresando al menú principal")
            break
        else:
            print("Opción inválida. Seleccione una correcta")
            

#Función menú principal 
def menu():
    while True: 
        opcion = int(input("¿Qué desea realizar el día de hoy? \n1. Listar archivos \n2. Procesar archivo (.txt) \n3. Procesar archivo (.csv) \n4. Salir"))
        if opcion == 1: 
            men_arch()
        elif opcion == 2: 
            menu_arch_txt()
        elif opcion == 3:
            men_arch_csv()
        elif opcion == 4:
            print("Saliendo del programa")
            break 
    else:
        print("Ingrese una opción correcta")

        

if __name__ == "__main__":
    menu()
