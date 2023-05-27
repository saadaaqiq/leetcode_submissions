# https://leetcode.com/problems/product-of-array-except-self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    l = [nums[0]]
    for i in range(1, n-1):
      l.append(l[-1]*nums[i])
    l.insert(0, 1)
    r = [1] * (n-2) + [nums[-1]]
    for i in range(n-3, -1, -1):
      r[i] = r[i+1] * nums[i+1]
    r.append(1)
    return [l[i]*r[i] for i in range(n)]
    