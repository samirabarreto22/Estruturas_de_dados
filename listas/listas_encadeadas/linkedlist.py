## sequencial = []
## sequencial.append(6)

## busca e acesso
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    """INSERIR ELEMENTOS AO FINAL DA LISTA"""
    def append(self, elem):
        if self.head:
            ## complexidade o(n)
            # inserção quando a lista ja possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)

        self._size = self._size + 1

    def __len__(self):
        ## retorna o tamanho da lista
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next    
            else:
                raise IndexError("List index out of range")
        return pointer
    
    def get(self, index):
        # a = lista.get(6)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of rangeee")
            
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of rangeee")

    def set(self, index, elem):
        # a = lista.set(5.9)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of rangeee")
            
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of rangeee")
    
    def __getitem__(self, index):
        # a = lista[6]
        # a = lista.get(6)
        # complexidade o(N)
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of rangeee")
                

    def __setitem__(self, index, elem):
        # lista[5] = 9
        # lista.set(5,9)
        # complexidade O(n)
        pointer = self._getnode(index)
            
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of rangeee")
        
    def index(self, elem):
        # complexidade O(n)
        """ADAPTAÇÃO BUSCA LINEAR"""
        """Retorna o indice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError(' isnot in list')
        
    def insert(self, index, elem):

        # complexidade O(n)

        node = Node(elem)
        ## usuario quer inserir no começo da lista
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
    
    def remove(self, elem):

        # complexidade O(n)
        if self.head is None:
            raise ValueError("{} is not in list".format(elem))

        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True

        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer is not None:
                if pointer.data == elem:
                    # Remove o elemento
                    ancestor.next = pointer.next
                    pointer.next = None
                    return True

                pointer = pointer.next
                ancestor = ancestor.next
            self._size = self._size - 1

        raise ValueError("{} is not in list".format(elem))
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r


    def __str__(self):
        return self.__repr__()

        

lista = LinkedList()
lista.append(7)
lista.append(9)
lista.append(6)
lista.append(80)
lista.append(5)
##print(len(lista))
##print(lista.get(0))
## lista.append(88)
## print(lista.index(88))
##lista.insert(3, 22)
#print(lista[3])
##print(lista[4])
#lista.insert(0, 15)
#print(lista[0])
#print(lista[1])
#lista.insert(len(lista), 50)
#print(lista[len(lista) - 1])
print(lista[3])


## OBS: perceba que "piorou" comparado a lista sequencial
## pois algoritmo variavel O(n)
