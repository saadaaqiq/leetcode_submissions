# https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n, res = len(s), 0
        arr = [[0, 0]]
        cur = s[0]
        for i in range(1, n):
            if s[i] == cur:
                arr[-1][1] = i
            else:
                cur = s[i]
                arr.append([i, i])
        if len(arr) == 1:
            return res
        for k in range(len(arr)-1):
            res += min(arr[k][1] - arr[k][0] + 1, arr[k+1][1] - arr[k+1][0] + 1)
        return res


