# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m, n = len(s), len(t)
        res, max_len_res = "", float("infinity")

        if m < n:
            return res

        ct = Counter(t)
        cs = Counter(s[:n])

        def first_counter_in_second(c1, c2):
            for k in c1:
                if c1[k] > 0:
                    if k not in c2 or c2[k] < c1[k]:
                        return False
            return True

        i, j = 0, n

        while j <= m:
            if first_counter_in_second(ct, cs):
                if j - i <= max_len_res:
                    max_len_res = j - i
                    res = s[i:j]
                cs[s[i]] -= 1
                i += 1
            else:
                if j == m:
                    break
                cs[s[j]] += 1
                j += 1
        

        return res



