# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
  
  def findCelebrity(self, n: int) -> int:
    
    i = 0
    for j in range(n):
      if knows(i,j):
        i = j

    def isCeleb(cand):
      for j in range(n):
        if j == i: continue
        if knows(i,j) or not knows(j,i):
          return False
      return True

    return i if isCeleb(i) else -1
    
