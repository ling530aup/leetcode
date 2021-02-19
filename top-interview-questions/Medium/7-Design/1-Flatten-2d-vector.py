from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.ls = []
        for line in v:
            for i in line:
                self.ls.append(i)

        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.ls[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.ls)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
