# https://leetcode.com/problems/sparse-matrix-multiplication

class Solution:
  def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    
    res = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        
    def compressA(M):
      elems = {i:{} for i in range(len(M))}
      for i in range(len(M)):
        for j in range(len(M[0])):
          if M[i][j] != 0:
            elems[i][j] = M[i][j]
      return elems
    
    def compressB(M):
      elems = {j:{} for j in range(len(M[0]))}
      for j in range(len(M[0])):
        for i in range(len(M)):
          if M[i][j] != 0:
            elems[j][i] = M[i][j]
      return elems
    
    cA = compressA(A)
    cB = compressB(B)
    
    for i in cA:
      for j in cB:
        s = 0
        for k in cA[i]:
          if k in cB[j]:
            s += cA[i][k] * cB[j][k]
        res[i][j] = s
    
    return res
      
      