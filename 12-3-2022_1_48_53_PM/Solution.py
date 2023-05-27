# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        res = ["" for _ in range(200)]
        for c in s:
            res[ord(c)] += c
        res.sort(key=lambda x:len(x), reverse=True)
        return "".join(res)