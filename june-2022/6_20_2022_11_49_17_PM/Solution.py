# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

  def __init__(self):
    self.left = []
    heapq.heapify(self.left)
    self.right = []
    heapq.heapify(self.left)
     
  def addNum(self, num: int) -> None:
    if len(self.left) == 0 and len(self.right) == 0:
      heapq.heappush(self.right, num)
    else:
      if num < self.right[0]:
        heapq.heappush(self.left, -num)
        while len(self.left) > len(self.right):
          heapq.heappush(self.right, -heapq.heappop(self.left))
      else:
        heapq.heappush(self.right, num)
        while len(self.right) > len(self.left) + 1:
          heapq.heappush(self.left, -heapq.heappop(self.right))
          
  def findMedian(self) -> float:
    if len(self.left) == len(self.right):
      return (-self.left[0] + self.right[0]) / 2
    else:
      return self.right[0]
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()