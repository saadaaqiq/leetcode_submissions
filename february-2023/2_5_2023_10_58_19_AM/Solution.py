# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        cp = Counter(p)
        cs = Counter(s[:len(p)])
        if cp == cs:
            res.append(0)
        for j in range(len(p), len(s)):
            cs[s[j-len(p)]] -= 1
            cs[s[j]] += 1
            if cp == cs:
                res.append(j-len(p)+1)
        return res
