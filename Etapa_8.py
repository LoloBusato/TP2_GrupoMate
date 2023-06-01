diccionario_csv={}

palabras=open('palabras.txt', 'r')
definiciones = open('definiciones.txt', 'r')
count_pal=0
count_def=0

def leer_pal(palabras,count_pal):
    linea_pal=palabras.readline()
    count_pal+=1
    return linea_pal,count_pal 


def leer_def(definiciones,count_def):
    linea_def=definiciones.readline()
    count_def+=1
    return linea_def,count_def 


def validar_palabra(palabra):
    validacion = True if palabra.isalnum() else False
    return validacion

def crear_diccionario(linea_1,count_1,linea_2,count_2):
    lista_indice=[]
    condicion=True
    while condicion:
        palabra,count_pal=leer_pal(palabras,count_pal)
        if validar_palabra(palabra):
    
                

