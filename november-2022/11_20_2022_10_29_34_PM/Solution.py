# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)
        i = 0
        while i < len(nums):
            for k in range(3):
                if k in counter and counter[k] > 0:
                    nums[i] = k
                    counter[k] -= 1
                    break
            i += 1
        