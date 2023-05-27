# https://leetcode.com/problems/binary-search

class Solution:
  
  def search(self, arr: List[int], x: int) -> int:
    
    def bs(l, r):
      if l > r:
        return -1
      else:
        m = (l+r)//2
        if x == arr[m]:
          return m
        elif x > arr[m]:
          return bs(m+1,r)
        else:
          return bs(l,m-1)
    
    return bs(0, len(arr)-1)
    