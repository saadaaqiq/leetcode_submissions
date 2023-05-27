# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        res = []
        for i in range(len(pivot)):
            for s in strs:
                if i >= len(s) or s[i] != pivot[i]:
                    return "".join(res)
            res.append(pivot[i])
        return "".join(res)