#-------------------------------------------------------------------------------------------------------------------
import chardet
#esta funcion la tuve que crear para resolver un problema que me saltaba en consola.
#esta en desuso igual, lo que esta en uso es la constante ENCODING
#la funcion encoding esta en cada open de archivos (hay 3) = ENCODING
def detectar_encoding(archivo):
    with open(archivo, 'rb') as formato:
       resultado = chardet.detect(formato.read())
    return resultado['encoding']

ENCODING='utf-8'

#-------------------------------------------------------------------------------------------------------------------

#LEE LOS ARCHIVOS.TXT LINEA POR LINEA
def leer_archivos(palabras,definiciones):
    linea_def=definiciones.readline().rstrip()
    linea_pal=palabras.readline().rstrip()
    return linea_pal,linea_def

#CREACION DE NUESTRO DICC ORDENADO ALF.   TYPE: LIST
def crear_diccionario(palabras,definiciones):
    dicc={}
    palabra,definicion=leer_archivos(palabras,definiciones)
    while palabra:
            #valido que la palabra sea alum.
            if palabra.isalnum() and len(palabra)>MINIMO:
                dicc[palabra]="'"+str(definicion)+"'"
            palabra,definicion=leer_archivos(palabras,definiciones)
    dicc=sorted(dicc.items(),key=lambda x:x[PALABRA])
    return dicc

#ESCRIBIR DICC
def escribir_dicc(dicc,linea):
    linea_str=','.join(linea) + '\n'
    dicc.write(linea_str)
#----------------------------------------------------------------------------------------------------------------
#GENERO VARIABLES Y CONSTANTES QUE VOY A USAR
PALABRA=0
MINIMO=4
#------------------------------------------------------------------------------------------------------------------------

#CREO EL ARCHIVO DICCIONARIO.CSV
def crear_diccionario_csv(nombre_archivo_pal,nombre_archivo_def):
    palabras = open(nombre_archivo_pal, 'r',encoding=ENCODING)
    definiciones = open(nombre_archivo_def, 'r',encoding=ENCODING)
    palabras_definiciones=crear_diccionario(palabras,definiciones)
    diccionario_csv = open('diccionario.csv','w',encoding=ENCODING)
    for linea in palabras_definiciones:
        escribir_dicc(diccionario_csv,linea)
    palabras.close()
    definiciones.close()    
    return diccionario_csv

crear_diccionario_csv("palabras.txt","definiciones.txt")
