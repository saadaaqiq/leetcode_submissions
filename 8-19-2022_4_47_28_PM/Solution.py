# https://leetcode.com/problems/brace-expansion

class Solution:
  def expand(self, s: str) -> List[str]:
    arr = [ w.split(',') for w in re.split('\{|\}', s) ]
    for i in range(len(arr)-2, -1, -1):
      a = []
      for c1 in arr[i]:
        for c2 in arr[i+1]:
          a.append(c1+c2)
      arr[i] = a
    return sorted(arr[0])
    
    
    
    
      
      
      
      
