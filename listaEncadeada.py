## Criando o No da lista
class Nor:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

## o primeiro no da lista serve como referencia a toda a lista
## função que imprime uma lista, usando como parametro apenas um no
def imprimeLista(no):
    while no:
        print(no, end=" -> ")
        no = no.next
    print("none")


#### testes
no1 = Nor(1)
no2 = Nor(2)
no3 = Nor(3)

## conectando os nós
no1.next = no2
no2.next = no3

imprimeLista(no1)




