# https://leetcode.com/problems/find-the-duplicate-number

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    slow = fast = 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    steps = 1
    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]
    second_slow = 0
    slow = nums[slow]
    second_slow = nums[second_slow]
    while slow != second_slow:
      slow = nums[slow]
      second_slow = nums[second_slow]
    return slow