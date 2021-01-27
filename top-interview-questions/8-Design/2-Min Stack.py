class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []

    def push(self, x: int) -> None:
        if self.getMin() < x:
            self.ls.append((x,self.getMin()))
        else:
            self.ls.append((x,x))

    def pop(self) -> None:
        return self.ls.pop()[0]

    def top(self) -> int:
        return self.ls[-1][0]

    def getMin(self) -> int:
        if not self.ls:
            return float("inf")
        return self.ls[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
