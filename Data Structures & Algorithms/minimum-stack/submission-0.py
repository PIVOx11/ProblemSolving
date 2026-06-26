class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        return None
    def pop(self) -> None:
        self.stack.pop(0)
        return None
    
    def top(self) -> int:
        return self.stack[0]  

    def getMin(self) -> int:
        return min(self.stack)
