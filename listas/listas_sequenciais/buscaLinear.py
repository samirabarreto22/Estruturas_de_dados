## acesso aleatorio
## numero constantes de operações o(1)

## buscar onde se encontra (index) o dado 
## complexidade linear o(n)(listas não ordenadas)
## buscar binaria = o(log n)

def busca(lista, elem):
    """Retorna o indice do elem se ele estiver na lista ou none, caso contrario"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = "python"

indice = busca(lista_estranha, elemento)

if indice is not None:
    print("O indice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista". format(elemento))