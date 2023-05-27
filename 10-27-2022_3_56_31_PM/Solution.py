# https://leetcode.com/problems/image-overlap

class Solution:
  def largestOverlap(self, A, B):
    return max(Counter([(c1[0]-c2[0],c1[1]-c2[1]) for c1 in [(i,j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j]==1] for c2 in [(i,j) for i in range(len(A)) for j in range(len(A[0])) if B[i][j]==1]]).values() or [0])