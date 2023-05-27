# https://leetcode.com/problems/container-with-most-water

class Solution:
  def maxArea(self, h):
    i, j, m = 0, len(h)-1, 0

    while i < j:
      m = max(m, min(h[i],h[j])*(j-i))
      if h[i] > h[j]:
        j -= 1
      else:
        i += 1
    return m