# https://leetcode.com/problems/product-of-array-except-self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    for i in range(1,n):
      answer[i] = answer[i-1]*nums[i-1]
    prev = 1
    for i in range(n-2, -1, -1):
      prev *= nums[i+1]
      answer[i] *= prev
      
    return answer

    