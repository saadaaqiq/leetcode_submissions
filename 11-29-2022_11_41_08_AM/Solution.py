# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
  def kthSmallest(self, mat: List[List[int]], k: int) -> int:
    return sorted([mat[i][j] for i in range(len(mat)) for j in range(len(mat))])[k-1]