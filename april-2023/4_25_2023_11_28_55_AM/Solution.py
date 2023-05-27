# https://leetcode.com/problems/smallest-number-in-infinite-set

class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1, 1001)]
        heapq.heapify(self.h)
        self.popped = set()

    def popSmallest(self) -> int:
        x = heapq.heappop(self.h)
        self.popped.add(x)
        return x

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
            heapq.heappush(self.h, num)