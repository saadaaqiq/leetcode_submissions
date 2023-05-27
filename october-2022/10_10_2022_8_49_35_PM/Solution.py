# https://leetcode.com/problems/max-chunks-to-make-sorted

class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    stack = []
    res = len(arr)
    for num in arr:
      last = num
      while stack and num < stack[-1]:
        last = max(last, stack.pop())
        res -= 1
      stack.append(last)
    return res
        
        