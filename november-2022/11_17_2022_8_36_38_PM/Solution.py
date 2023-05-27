# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        i, j = 0, len(p)
        pcount = Counter(p)
        scount = Counter(s[i:j])
        while j <= len(s):
            if pcount == scount:
                res.append(i)
            if j == len(s): break
            scount[s[i]] -= 1
            if scount[s[i]] == 0:
                scount.pop(s[i])
            i += 1
            if s[j] not in scount:
                scount[s[j]] = 0
            scount[s[j]] += 1
            j += 1
        return res