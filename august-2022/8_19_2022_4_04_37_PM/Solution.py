# https://leetcode.com/problems/brace-expansion

class Solution:
  def expand(self, s: str) -> List[str]:
    arr = []
    inside = False
    curr = []
    for c in s:
      if c == '{':
        inside = True
        continue
      if c == '}':
        inside = False
        arr.append(curr)
        curr = []
        continue
      if inside:
        if c != ',':
          curr.append(c)
      else:
        curr.append(c)
        arr.append(curr)
        curr = []
    
    for i in range(len(arr)-2, -1, -1):
      a = []
      for c in arr[i]:
        for cp in arr[i+1]:
          a.append(c + cp)
      arr[i] = a
      
    return sorted(arr[0])
      
      
      
      
      
