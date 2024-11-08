import csv 
import matplotlib.pyplot as plt 
import os 

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
            else:  
                print("Ingrese una columna válida") 

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



            

                


#Función menú principal 
def menu():
    while True: 
        opcion = int(input("¿Qué desea realizar el día de hoy? \n1. Listar archivos \n2. Procesar archivo (.txt) \n3. Procesar archivo (.csv) \n4. Salir"))
        if opcion == "2": 
            menu_arch_txt()



if __name__ == "__main__":
    menu()
