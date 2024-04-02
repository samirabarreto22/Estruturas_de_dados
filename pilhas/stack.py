from node import Node

# inserir na pilha
# remover na pilha
# observar o topo da pilha
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self,elem):
        # inserir um elemento na pilha
        # complexidade O(1)
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        # complexidade O(1)
        if self._size > 0:

            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        
        raise IndexError("The stack is empty")

    def peek(self):
        # retorna o topo sem remover
        # complexidade O(1)
        if self._size > 0:
            return self.top
        raise IndexError("The stack is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

pilha = Stack()
print(len(pilha))
print(pilha)

pilha.push(3)
pilha.push(7)
pilha.push("python")
pilha.push(True)
pilha.push("sucesso")
pilha.push(1.2)
print(pilha)
pilha.peek()
pilha.pop()
print(pilha)
        
