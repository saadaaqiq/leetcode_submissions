# https://leetcode.com/problems/boats-to-save-people

class Solution:
    def numRescueBoats(self, arr: List[int], k: int) -> int:
        res = 0
        arr.sort()
        l, r = 0, len(arr) - 1
        while l <= r:
            if l == r:
                return res + 1
            if arr[l] + arr[r] <= k:
                l += 1
            res += 1
            r -= 1
        return res