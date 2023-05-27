# https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        n = len(s)
        i, j = 0, 0
        res = 0
        while j < n:
            sm = sum(arr)
            mx = max(arr)
            if sm - mx <= k:
                res = max(res, sm)
                arr[ord(s[j])-65] += 1
                j += 1
            elif sm - mx > k:
                arr[ord(s[i])-65] -= 1
                i += 1
        if sum(arr) - max(arr) <= k:
            res = max(res, sum(arr))
        return res
                