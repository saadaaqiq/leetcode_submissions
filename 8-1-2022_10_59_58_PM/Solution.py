# https://leetcode.com/problems/robot-bounded-in-circle

class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    points = []
    current = (0,0)
    steps = [(0,1), (1,0), (0,-1), (-1,0)]
    d = 0
    
    def execute(point, direction):
      current = point
      d = direction
      for c in instructions:
        if c == 'G':
          current = tuple(map(lambda x, y: x + y, current, steps[d]))
        if c == 'L':
          d = (d - 1) % 4
        if c == 'R':
          d = (d + 1) % 4
      return current, d
    
    i = 0
    while i < 4:
      current, d = execute(current, d)
      i += 1
    return current == (0,0)