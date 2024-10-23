from poblacion import * 
def imprime_datos_tabulados(lista):
    for e in lista: 
        print("/t", e )
def test_lee_poblaciones(registro): 
    print("==> Test de la función lee_poblaciones")
    print(f"Se han leido {len(registro)} datos")
    print("==> Mostramos los 4 primeros datos: ")
    imprime_datos_tabulados(registro[:4])
    print("==> Mostramos los 4 últimos datos:")
    imprime_datos_tabulados(registro[-4:])

def test_calcula_paises(lista_paises): 
    print(f"==>Aquí tenemos una lista ordenada con los nombres de los países: {lista_paises}")
    print (f"==>Se han leído {len(lista_paises)}")

def test_filtra_por_paises(poblaciones): 
    print(f"==>Aquí se muestran los datos del año y el censo: {poblaciones}")

def test_filtrar_por_paises_y_año(paises_y_año): 
    print(f"Se muestra la población del país en el año indicado: {paises_y_año}")

def test_muestra_evolucion_poblacion(grafica): 
    print(grafica)

def test_muestra_comparativa_paises_año(graf2): 
    print(graf2)
if __name__=='__main__': 
    datos=lee_poblaciones('data/population.csv')
    test_lee_poblaciones(datos)
    lista_paises=calcula_paises(datos)
    test_calcula_paises(lista_paises)
    poblaciones=filtra_por_pais(datos,"Zimbabwe")
    test_filtra_por_paises(poblaciones)
    paises_y_año=filtrar_por_paises_y_año(datos,2000,"Arab World, Zimbabwe, East Asia & Pacific")
    test_filtrar_por_paises_y_año(paises_y_año)
    grafica=muestra_evolucion_poblacion(datos,"Zimbabwe")
    test_muestra_evolucion_poblacion(grafica)
    graf2=muestra_comparativa_paises_año(datos,1960,("Central Europe and the Baltics","Arab World","Caribbean small states","Early-demographic dividend","East Asia & Pacific"))
    test_muestra_comparativa_paises_año(graf2)
    