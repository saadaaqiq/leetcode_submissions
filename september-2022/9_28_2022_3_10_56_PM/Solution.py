# https://leetcode.com/problems/majority-element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    # print('https'+':'+'/'+'/'+'en'+'.'+'wikipedia'+'.'+'org'+'/'+'wiki'+'/'+'Boyer-Moore_majority_vote_algorithm')
    count, res = 0, 0
    for num in nums:
      if count == 0:
        res, count = num, 1
      elif num == res:
        count += 1
      else:
        count -= 1
    return res