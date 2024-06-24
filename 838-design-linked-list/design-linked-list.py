class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current == None:
                return -1
            current = current.next
        if current == None:
            return -1
        return current.value
        

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
        aux = Node(val)
        current = self.head
        if current == None:
            return
        for i in range(index - 1):
            if current == None or current.next == None:
                return
            current = current.next
        if self.tail == current:
            self.addAtTail(val)
            return
        aux.next = current.next
        current.next = aux


    def deleteAtIndex(self, index: int) -> None:
        print(index)
        if index == 0:
            if self.tail == self.head:
                self.tail = self.head.next
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        if current == None:
            return
        if self.tail == current.next:
            self.tail = current
            current.next = None
            return
        if current != None:
            if current.next != None:
                current.next = current.next.next
            else:
                current.next = None
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)