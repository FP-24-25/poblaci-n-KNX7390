import csv 
from collections import namedtuple
import matplotlib.pyplot as plt
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
def calcula_paises(poblaciones): 
    lista_pueblos=set()
    for pueblo in poblaciones:
        lista_pueblos.add(pueblo.pais)
        lista_paises=list(lista_pueblos)
        lista_paises.sort()
    return lista_paises    

def filtra_por_pais(poblacion,nombre_o_codigo):
    res = []
    for pais in poblacion:
           if pais.codigo == nombre_o_codigo or pais.pais == nombre_o_codigo:
               res.append((pais.año, pais.censo))
    return res
def filtrar_por_paises_y_año(poblaciones,año,paises): 
    tupla=[] 
    for variable in poblaciones:
        if variable.pais in paises and variable.año==año:  
            tupla.append((variable.pais,variable.censo))
    return tupla

def muestra_evolucion_poblacion(poblaciones,nombre_o_codigo):
    titulo="Esta es la gráfica que representa la evolución de la poblacion"
    lista_años=[]
    lista_habitantes=[]
    for i in poblaciones:
        if i.codigo==nombre_o_codigo or i.pais==nombre_o_codigo: 
            lista_años.append(i.año)
            lista_habitantes.append(i.censo)
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_año(poblaciones,año,paises): 
    titulo="Esta es la gráfica que compara la evolución de la población"
    lista_paises=sorted([])
    lista_habitantes=[]
    paises=set(paises)
    for var in poblaciones: 
            for pais in paises:
                if pais==var.pais and año==var.año: #problemas con el operador
                    lista_paises.append(var.pais)
                    lista_habitantes.append(var.censo)
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()

        
        

        

     
       