# https://leetcode.com/problems/merge-sorted-array

class Solution:
  def merge(self, nums1, m, nums2, n):
    h = []
    for i in range(m):
      heapq.heappush(h, nums1[i])
    for j in range(n):
      heapq.heappush(h, nums2[j])
    for i in range(m+n):
      nums1[i] = heapq.heappop(h)
    