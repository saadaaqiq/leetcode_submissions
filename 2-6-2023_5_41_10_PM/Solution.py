# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        dec = collections.deque()
        inc = collections.deque()
        l, r = 0, 0
        res = 0
        while r < N:
            while inc and nums[r] < nums[inc[-1]]:
                inc.pop()
            while dec and nums[r] > nums[dec[-1]]:
                dec.pop()
            inc.append(r)
            dec.append(r)
            while dec and inc and abs(nums[dec[0]] - nums[inc[0]]) > limit:
                if inc and inc[0] == l:
                    inc.popleft()
                if dec and dec[0] == l:
                    dec.popleft()
                l += 1 
            res = max(res, r-l+1)
            r += 1
        return res




