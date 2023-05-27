# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, i, j, res = len(s), 0, 0, 0
        vis = set()
        while j < n:
            if s[j] not in vis:
                vis.add(s[j])
                j += 1
            else:
                vis.remove(s[i])
                i += 1
            res = max(res, j-i)
        return res