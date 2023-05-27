# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {num: i for (i, num) in enumerate(nums)}
        for i, x in enumerate(nums):
            if target - x in dic and dic[target-x] != i:
                return [i, dic[target-x]]
        