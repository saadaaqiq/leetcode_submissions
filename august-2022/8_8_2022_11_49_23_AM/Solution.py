# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
  
  def findCelebrity(self, n: int) -> int:
    
    i, j = 0, 0
    known = set()
    notKnown = set()
    
    while i < n and j < n:
      if i == j:
        j += 1
        continue
      if knows(i,j):
        known.add((i,j))
        i += 1
      else:
        notKnown.add((i,j))
        j += 1

    if i >= n:
      return -1
    
    for j in range(n):
      if j!=i:
        if (i,j) in known or (j,i) in notKnown:
          return -1
        if knows(i,j) or not knows(j,i):
          return -1

    return i
    
