class Node:
    def __init__(self, val: int, last_min):
        self.val = val
        self.last_min = last_min

    def __str__(self):
        return f"val:{self.val}, last_min:{self.last_min}"

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = Node(float('inf'), None)

    def push(self, val: int) -> None:
        x = Node(val, self.min)
        self.stack.append(x)
        if val < self.min.val:
            self.min = x
        
    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.min:
            self.min = self.min.last_min

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.min.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()