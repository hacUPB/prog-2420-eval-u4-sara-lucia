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
            




#Función submenú 
def menu_arch_txt():
    while True: 
        opcion_texto = int(input("Seleccione la opción que desea realizar. \n1. Contar número de palabras \n2. Reemplazar una palabra por otra \n3. Contar numero de caracteres \n4. Menú principal"))
        if opcion_texto == 1:

    


#Función menú principal 
def menu():
    while True: 
        opcion = int(input("¿Qué desea realizar el día de hoy? \n1. Listar archivos \n2. Prosesar archivo (.txt) \n3. Procesar archivo (.csv) \n4. Salir"))


if __name__ == "__main__":
    menu()
