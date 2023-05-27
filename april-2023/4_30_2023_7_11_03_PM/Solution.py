# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        m,n=len(s),len(t)
        g = gcd(m,n)
        if (m//g) * s[:g] == s and (n//g) * t[:g] == t and s[:g] == t[:g]:
            return s[:g]
        else:
            return ''