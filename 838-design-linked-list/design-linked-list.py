class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        res = self.__get_node(index)
        if res == None:
            return -1
        return res.value
    
    def __get_node(self, index: int) -> Node:
        current = self.head
        for i in range(index):
            if current == None:
                return None
            current = current.next
        return current
        

    def addAtHead(self, val: int) -> None:
        aux = Node(val)
        aux.next = self.head
        if not self.tail:
            self.tail = aux
        self.head = aux

    def addAtTail(self, val: int) -> None:
        aux = Node(val)
        if self.tail:
            self.tail.next = aux
        if not self.head:
            self.head = aux
        self.tail = aux

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        # the node before
        node = self.__get_node(index - 1)
        if node == None:
            return
        if node == self.tail:
            self.addAtTail(val)
            return
        aux = Node(val)
        aux.next = node.next
        node.next = aux

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.tail == self.head:
                self.tail = self.head.next
            self.head = self.head.next
            return
        node = self.__get_node(index - 1)
        if node == None or node.next == None:
            return
        if node.next == self.tail:
            self.tail = node
        node.next = node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)