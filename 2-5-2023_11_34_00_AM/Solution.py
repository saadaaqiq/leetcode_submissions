# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        res_length = math.inf
        res = ""
        i, j = 0, n
        cs, ct = Counter(s[:n]), Counter(t)
        while True:
            while i < j and cs >= ct:
                if j - i < res_length:
                    res = s[i:j]
                    res_length = j - i
                cs[s[i]] -= 1
                i += 1
            if j == m:
                break
            cs[s[j]] += 1
            j += 1
        return res



