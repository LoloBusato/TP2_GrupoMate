#----------------------------------------------------------------------------------------------------------------
#GENERO VARIABLES Y CONSTANTES QUE VOY A USAR
TAMANIO = 5

#LEE LOS ARCHIVOS.TXT LINEA POR LINEA
def leer_archivo(archivo):
    linea = archivo.readline().rstrip()
    return linea if linea else "" #Devuelve 1 vacio

def grabar_archivo(archivo, diccionario):
    PALABRA = 0
    DEFINICION = 1
    for pal_def in diccionario:
        archivo.write(pal_def[PALABRA] + ',' + pal_def[DEFINICION] + '\n')

#CREACION DE NUESTRO DICC ORDENADO ALF.   TYPE: LIST
def crear_diccionario(archivo_pal,archivo_def):
    dicc=[]
    palabra = leer_archivo(archivo_pal)
    definicion = leer_archivo(archivo_def)
    while palabra and definicion:
        #valido que la palabra contenga solo letras y tenga un tamaño mayor al pedido
        if palabra.isalpha() and len(palabra) >= TAMANIO:
            dicc.append([palabra, definicion])
            palabra = leer_archivo(archivo_pal)
            definicion = leer_archivo(archivo_def)
        else:   
            palabra = leer_archivo(archivo_pal)
            definicion = leer_archivo(archivo_def)
    dicc.sort(key = lambda x: x[0])
    return dicc

#------------------------------------------------------------------------------------------------------------------------

palabras_txt = open("palabras.txt", "r", encoding="utf8")
definiciones_txt = open("definiciones.txt", "r", encoding="utf8")
diccionario_txt = open("diccionario.csv", "w", encoding="utf8")
palabras_definiciones = crear_diccionario(palabras_txt,definiciones_txt)
grabar_archivo(diccionario_txt, palabras_definiciones)
definiciones_txt.close()
palabras_txt.close()
diccionario_txt.close()

