
# Name: Min Stack
# Link: https://leetcode.com/problems/min-stack/
# Method: Use a secondary stack, that holds the minimum element
# Time: O(1)
# Space: O(n)
# Difficulty: Medium

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack and self.minStack[-1] < x:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)

    obj.push(3)
    print(obj.getMin())
