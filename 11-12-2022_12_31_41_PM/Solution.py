# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:
    def __init__(self):
        self.left = []
        heapq.heapify(self.left)
        self.right = []
        heapq.heapify(self.right)

    def calibrate(self, l, r):
        while len(l) < len(r) - 1:
            heapq.heappush(l, -heapq.heappop(r))
        while len(l) > len(r):
            heapq.heappush(r, -heapq.heappop(l))

    def addNum(self, num: int) -> None:
        if not self.right or num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        self.calibrate(self.left, self.right)


    def findMedian(self) -> float:
        if len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2

