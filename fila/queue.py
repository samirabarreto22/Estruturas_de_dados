from node import Node

# inserir na pilha
# remover na pilha
# observar o topo da pilha
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        # inserir um elemento na pilha
        # complexidade O(1)
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        
        self._size = self._size + 1
        
    def pop(self):
        # remove o elemento do topo da pilha
        # complexidade O(1)
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem

        raise IndexError("The queue is empty")

    def peek(self):
        # retorna o topo sem remover
        # complexidade O(1)
        if self.first is not None:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")
  

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        if self._size > 0:

            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "empty queue"

    def __str__(self):
        return self.__repr__()
    
fila = Queue()
print(fila)
fila.push(5)
fila.push(9)
fila.push("samira")
fila.push(True)
fila.push(42)
print(fila)
fila.pop()
print(fila)
print(fila.peek())