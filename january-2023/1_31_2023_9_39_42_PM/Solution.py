# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            ind = bisect_left(res, num)
            if ind == len(res):
                res.append(num)
            else:
                res[ind] = num
        return len(res)    
