# https://leetcode.com/problems/car-fleet

class Solution:
  def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
    n = len(p)
    cars = sorted([(p[i], (t-p[i])/s[i]) for i in range(n)], key= lambda c: c[0])
    stack = []
    
    for i in range(n-1, -1, -1):
      while stack and cars[stack[-1]][1] >= cars[i][1]:
        cars[i] = cars[i][0], cars[stack.pop()][1]
      stack.append(i)
    
    return len(stack)