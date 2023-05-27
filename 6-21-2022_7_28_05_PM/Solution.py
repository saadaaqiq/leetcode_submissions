# https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = [ (-num, i) for (i,num) in enumerate(nums) ]
    heapq.heapify(heap)
    i = 1
    while i < k:
      heapq.heappop(heap)
      i += 1
    return -heapq.heappop(heap)[0]