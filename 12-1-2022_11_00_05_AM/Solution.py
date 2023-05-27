# https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        c1, c2 = Counter(s[:len(s)//2]), Counter(s[len(s)//2:])
        ca, cb = 0, 0
        for v in vowels:
            if v in c1:
                ca += c1[v]
            if v in c2:
                cb += c2[v]
        return ca == cb