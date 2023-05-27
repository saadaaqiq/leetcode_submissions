# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {target - x: i for (i,x) in enumerate(nums)}
        for j, y in enumerate(nums):
            if y in dic and dic[y] != j:
                return [dic[y],j]
        