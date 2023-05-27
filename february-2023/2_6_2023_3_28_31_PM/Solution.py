# https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0
        while i < n:
            res.append(nums[i])
            res.append(nums[i+n])
            i += 1
        return res