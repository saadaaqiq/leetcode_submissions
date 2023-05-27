# https://leetcode.com/problems/arithmetic-slices-ii-subsequence

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: 
            return 0
        dic = [defaultdict(int) for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                sub = nums[i] - nums[j] 
                prev = dic[j][sub] 
                res += prev
                dic[i][sub] += prev + 1
        
        return res



