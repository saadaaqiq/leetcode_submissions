# https://leetcode.com/problems/find-smallest-common-element-in-all-rows

class Solution:
  def smallestCommonElement(self, mat: List[List[int]]) -> int:
    pointers = [0 for i in range(len(mat))]
    while True:
      m = max([mat[i][pointers[i]] for i in range(len(mat))])
      for i in range(len(mat)):
        while pointers[i]<len(mat[0]) and mat[i][pointers[i]] < m:
          pointers[i] += 1
        if pointers[i] == len(mat[0]):
          return -1
      boo = True
      for i in range(len(mat)):
        if mat[i][pointers[i]] != m:
          boo = False
          break
      if boo:
        return mat[0][pointers[0]]
      
        