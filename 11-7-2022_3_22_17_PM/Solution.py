# https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [c for c in str(num)]
        for i, c in enumerate(s):
            if c == "6":
                s[i] = "9"
                break
        return int("".join(s))
