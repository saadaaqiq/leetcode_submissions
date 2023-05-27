# https://leetcode.com/problems/minimize-maximum-of-array

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        m, s, c = 0, 0, 0
        for x in nums:
            s, c = s + x, c + 1
            if x > m:
                m = max(m, math.ceil(s/c))
        return m
            