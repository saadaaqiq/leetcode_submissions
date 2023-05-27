# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:
    def __init__(self):
        self.arr = []
        self.added = False

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.added = True

    def findMedian(self) -> float:
        n = len(self.arr)
        arr = self.arr
        if self.added:
            arr.sort()
            self.added = False
        return arr[n//2] if n%2==1 else (arr[(n-1)//2] + arr[(n+1)//2])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()