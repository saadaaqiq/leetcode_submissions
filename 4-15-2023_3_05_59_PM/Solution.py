# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        l, r = 0, n-1
        while l < r:
            res = max(res, (r-l)*min(arr[l],arr[r]))
            l, r = (l+1, r) if arr[l] <= arr[r] else (l, r-1)
        return res