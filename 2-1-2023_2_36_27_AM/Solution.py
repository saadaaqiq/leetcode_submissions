# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        p, q = len(str1), len(str2)
        gcd = math.gcd(p,q)
        if str1[:gcd] * (p // gcd) == str1 and str2[:gcd] * (q // gcd) == str2 and str1[:gcd] == str2[:gcd]:
            return str1[:gcd]
        else:
            return ""