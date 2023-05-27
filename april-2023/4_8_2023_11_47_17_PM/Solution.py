# https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for k in counter:
            if counter[k] % 2 == 1:
                return False
        return True