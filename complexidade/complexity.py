## exemplo para entender o conceito de complexidade

def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range (limite):
        aux = lista[i]
        lista[i] = lista[n-1]
        lista[tamanho-i] = aux

# 1 - vamos começar calculando a quantiade de alocação de memoria
# contar as variaveis
        # 4 + N (sendo N a lista) - complexidade de espaço
        # obs: a var aux não aumenta a quantidade de
        # memoria por causa do loop, pois o valor dela
        # se probepoem a cada laço

# 2 - calculando o processamento
        # calculamos as operações elementares
        # ( operações dentro de outras)
        # 2 + 4 * (N/2) - complexidade de tempo

# obs: os dois calculos dependem do tamanho da lista
        # a lista é a entrada do algoritmo
        # as operações com a lista é a saida

# obs: importante a complexidade de tempo
        # pois o que vale a pena em um algoritmo
        # é saber quanto tempo vamos precisar e se vai valer a pena esperar

def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range (tamanho):
        nova_lista.append(lista[tamanho - i])
    return nova_lista

# 2 + N tempo
# 3 + 3 N espaço


# 1 - a complexidade cresce de acordo com a entrada
# 2 - nos expressamos a complexidade com O
# 3 - calcular a complexidade do pior caso (teto)
