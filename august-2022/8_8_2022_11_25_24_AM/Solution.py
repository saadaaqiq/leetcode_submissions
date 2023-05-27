# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
  
  def findCelebrity(self, n: int) -> int:
    
    i, j = 0, 0
    
    while i < n and j < n:
      if i == j:
        j += 1
        continue
      i_knows_j = knows(i,j)
      if i_knows_j:
        i += 1
      else:
        j += 1

    if i < n:
      for j in range(n):
        if j!=i and (not knows(j,i) or knows(i,j)):
          return -1
        
    return i
    
