class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.cumin = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.cumin and self.cumin[-1] < x:
            self.cumin.append(self.cumin[-1])
        else:
           self.cumin.append(x) 
    
    def pop(self) -> None:
        self.stack.pop()
        self.cumin.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cumin[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
        
    obj.push(3)
    print(obj.getMin())
    
