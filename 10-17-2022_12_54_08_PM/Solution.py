# https://leetcode.com/problems/evaluate-division

class Solution:
  
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
    res, p, r, c = [], {}, {}, {}
    alone = set()
    not_alone = set()
    
    for i, eq in enumerate(equations):
      x, y = eq[0], eq[1]
      v = values[i]
      if x == y: alone.add(x)
      else:
        not_alone.add(x)
        not_alone.add(y)
      if x not in p:      p[x], r[x], c[x] = x, 1, 1
      if y not in p:      p[y], r[y], c[y] = y, 1, 1
      px, py, cx, cy = x, y, 1, 1
      while px != p[x]:   px = p[x]
      while py != p[y]:   py = p[y]
      if r[px] > r[py]:   p[py], c[py], r[px] = p[px], (v * c[x] / c[y]), r[px] + 1
      elif r[px] < r[py]: p[px], c[px], r[py] = p[py], (c[y] / (v * c[x])), r[py] + 1
      else:
        if px < py: p[py], c[py], r[px] = p[px], (v * c[x] / c[y]), r[px] + 1
        elif px > py: p[px], c[px], r[py] = p[py], (c[y] / (v * c[x])), r[py] + 1
        
    for a in not_alone:
      if a in alone:
        alone.remove(a)
        
    for x, y in queries:
      if x not in p or y not in p or (x == y and x in alone): res.append(-1)
      else:
        px, py, cx, cy = p[x], p[y], c[x], c[y]
        while px != p[px]: 
          cx *= c[px]
          px = p[px]
        while py != p[py]: 
          cy *= c[py]
          py = p[py]
        if px == py: res.append(cy/cx)
        else: res.append(-1)

    return res