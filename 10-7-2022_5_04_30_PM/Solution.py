# https://leetcode.com/problems/next-greater-element-i

class Solution:
  def nextGreaterElement(self, nums1, nums2):
    ans = deque()
    for i in range(len(nums1)-1, -1, -1):
      j = len(nums2)-1
      bigger = -1
      while nums2[j] != nums1[i]:
        if nums2[j]>nums1[i]:
          bigger = nums2[j]
        j -= 1
      ans.appendleft(bigger)
    return ans      
      