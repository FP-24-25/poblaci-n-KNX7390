import csv 
from collections import namedtuple
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_fichero): 
    resultado=[]
    with open(ruta_fichero) as f: 
        lector=csv.reader(f)
        for pais,codigo,año,censo in lector: 
            año=int(año)
            censo=int(censo)
            tupla=RegistroPoblacion(pais,codigo,año,censo)
            resultado.append(tupla)
    return resultado
def calcula_paises(registro_poblacion): 
    lista_pueblos=set()
    for pueblo in registro_poblacion:
        lista_pueblos.add(pueblo.pais)
        conjunto_paises=list(lista_pueblos)
        conjunto_paises.sort()
    return conjunto_paises
def filtra_por_pais(poblaciones,nombre_o_codigo): 
    for 