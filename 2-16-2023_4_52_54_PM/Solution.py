# https://leetcode.com/problems/constrained-subsequence-sum

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        h = []
        res = math.inf

        for i, x in enumerate(nums):
            while h and (i - h[0][1] > k or h[0][0] > 0):
                res = min(res, heapq.heappop(h)[0])
            heapq.heappush(h, (-x + (h[0][0] if h else 0), i))
        
        res = min(res, h[0][0] if h else math.inf)

        return - res