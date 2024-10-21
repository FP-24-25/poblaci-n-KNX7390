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

def test_calcula_paises(conjunto_paises): 
    print(f"==>Aquí tenemos una lista ordenada con los nombres de los países: {conjunto_paises}")
    print (f"==>Se han leído {len(conjunto_paises)}")
if __name__=='__main__': 
    datos=lee_poblaciones('data/population.csv')
    test_lee_poblaciones(datos)
    conjunto_paises=calcula_paises(datos)
    test_calcula_paises(conjunto_paises)