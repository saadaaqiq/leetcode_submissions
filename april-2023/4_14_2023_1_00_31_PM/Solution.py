# https://leetcode.com/problems/design-an-ordered-stream

class OrderedStream:

    def __init__(self, n: int):
        self.arr = ["" for _ in range(n+1)]
        self.r = 1
        self.l = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        while self.r < len(self.arr) and self.arr[self.r]:
            self.r += 1
        res = self.arr[self.l:self.r]
        self.l = self.r
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)