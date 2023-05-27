# https://leetcode.com/problems/flatten-2d-vector

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vector = []
        for arr in vec:
            for num in arr:
                self.vector.append(num)
        self.i = -1
        self.n = len(self.vector)

    def next(self) -> int:
        if self.i < self.n - 1:
            self.i += 1
            return self.vector[self.i]
        
    def hasNext(self) -> bool:
        return self.i < self.n - 1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()