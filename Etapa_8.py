import csv
#-------------------------------------------------------------------------------------------------------------------
import chardet
#esta funcion la tuve que crear para resolver un problema que me saltaba en consola.
#si no es necesaria pueden probarlo solamente elimando:
#-ecoding_palabras,encoding_definiciones y sus respectivos encoding en los open.
def detectar_encoding(archivo):
    with open(archivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']
encoding_palabras = detectar_encoding('palabras.txt')
encoding_definiciones = detectar_encoding('definiciones.txt')
#encoding_dicc = detectar_encoding('diccionario.csv') 
#-------------------------------------------------------------------------------------------------------------------

#ABRIMOS LOS ARCHIVOS.TXT
palabras_txt = open('palabras.txt', 'r', encoding=encoding_palabras)
definiciones_txt = open('definiciones.txt', 'r', encoding=encoding_definiciones)

#GENERO VARIABLES Y CONSTANTES QUE VOY A USAR
count_pal=0
count_def=0
PALABRA=0

#LEE LOS ARCHIVOS.TXT LINEA POR LINEA
def leer_pal(palabras,indice_pal):
    linea_pal=palabras.readline().rstrip()
    indice_pal+=1
    return linea_pal,indice_pal 

def leer_def(definiciones,indice_def):
    linea_def=definiciones.readline().rstrip()
    indice_def+=1
    return linea_def,indice_def 

#CREACION DE NUESTRO DICC ORDENADO ALF.   TYPE: LIST
def crear_diccionario(palabras,definiciones):
    indice_pal=0
    indice_def=0
    dicc={}
    palabra,indice_pal=leer_pal(palabras,indice_pal)
    definicion,indice_def =leer_def(definiciones,indice_def)
    while palabra:
            #valido que la palabra sea alum.
            if palabra.isalnum():
                if indice_def==indice_pal:
                    dicc[palabra]="'"+ str(definicion)+"'"
                    definicion,indice_def =leer_def(definiciones,indice_def)
                    palabra,indice_pal=leer_pal(palabras,indice_pal)
                else:
                    definicion,indice_def =leer_def(definiciones,indice_def)
            else:
                palabra,indice_pal=leer_pal(palabras,indice_pal)
    
    dicc=sorted(dicc.items(),key=lambda x:x[PALABRA])
    return dicc

#CREO EL ARCHIVO DICCIONARIO.CSV
palabras_definiciones = crear_diccionario(palabras_txt,definiciones_txt)
def crear_diccionario_csv(palabras_definiciones):
    diccionario_csv = 'diccionario.csv'
    #escribir los datos en el archivo CSV
    with open(diccionario_csv, 'w', newline='',encoding='utf-8') as dicc_csv:
        escritor = csv.writer(dicc_csv)
        escritor.writerows(palabras_definiciones)
    return diccionario_csv

crear_diccionario_csv(palabras_definiciones)

