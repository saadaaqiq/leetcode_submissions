# https://leetcode.com/problems/product-of-array-except-self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:

    def accuLeft(nums):
      arr = []
      for num in nums:
        if not arr:
          arr.append(num)
        else:
          arr.append(arr[-1]*num)
      return [1] + arr[:len(arr)-1]

    def accuRight(nums):
      q = deque()
      for num in reversed(nums):
        if not q:
          q.appendleft(num)
        else:
          q.appendleft(num * q[0])
      return list(q)[1:] + [1]

    l, r = accuLeft(nums), accuRight(nums)
    return [l[i]*r[i] for i in range(len(nums))]
    