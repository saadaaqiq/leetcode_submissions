# https://leetcode.com/problems/find-anagram-mappings

class Solution:
  def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
    dic = {}
    for i,num in enumerate(nums2):
      if num not in dic:
        dic[num] = []
      dic[num].append(i)
    res = []
    for num in nums1:
      res.append(dic[num].pop())
    return res