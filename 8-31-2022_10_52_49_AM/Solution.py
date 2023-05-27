# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
  def search(self, reader: 'ArrayReader', target: int) -> int:
    l = 0 
    r = 10**4 - 1
    while l <= r:
      mid = (l + r) // 2
      if reader.get(mid) > target:
        r = mid - 1
      elif reader.get(mid) < target:
        l = mid + 1
      else:
        return mid
    return -1