# https://leetcode.com/problems/boats-to-save-people

class Solution:
    def numRescueBoats(self, arr: List[int], limit: int) -> int:
        res = 0
        arr.sort()
        l, r = 0, len(arr)-1
        while l <= r:
            if arr[l] + arr[r] <= limit:
                l += 1
            r -= 1
            res += 1
        return res