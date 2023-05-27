# https://leetcode.com/problems/robot-bounded-in-circle

class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    points = []
    current = (0,0)
    d = 0
    def execute(point, direction):
      current, d = point, direction
      for c in instructions:
        if c == 'G':
          if d == 0:
            current = (current[0], current[1]+1)
          elif d == 1:
            current = (current[0]+1, current[1])
          elif d == 2:
            current = (current[0], current[1]-1)
          elif d == 3:
            current = (current[0]-1, current[1])
        else:
          d = (d - 1) % 4 if c == 'L' else (d + 1) % 4
      return current, d
    
    i = 0
    while i < 4:
      current, d = execute(current, d)
      i += 1
    return current == (0,0)