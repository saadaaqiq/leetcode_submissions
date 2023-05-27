# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        i, j = 0, 0
        counter = collections.Counter()
        for j in range(n):
            counter[s[j]] += 1
            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
