# https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        for c in s:
            if c == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(c)
        for c in t:
            if c == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(c)
        return "".join(s1) == "".join(s2)