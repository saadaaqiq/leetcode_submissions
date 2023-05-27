# https://leetcode.com/problems/image-overlap

class Solution:
  def largestOverlap(self, A, B):
    m,n = len(A), len(A[0])
    arr1 = [(i,j) for i in range(m) for j in range(n) if A[i][j]==1]
    arr2 = [(i,j) for i in range(m) for j in range(n) if B[i][j]==1]
    cnt = Counter([(c1[0]-c2[0],c1[1]-c2[1]) for c1 in arr1 for c2 in arr2])
    return max(cnt.values() or [0])