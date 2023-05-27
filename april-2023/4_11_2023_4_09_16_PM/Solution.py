# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # ignore leading white spaces
        while i < n and s[i] == ' ':
            i += 1

        # read sign
        negative = False
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            negative = True
            i += 1
        
        # ignore zeroes after sign or if not sign
        while i < n and s[i] == '0':
            i += 1
        
        # read digits
        arr = []
        while i < min(n, i+11) and s[i].isnumeric():
            arr.append(s[i])
            i += 1

        # if no digits then return
        if not arr:
            return 0
        
        # if digits
        NUM = int(''.join(arr))
        
        return max(-2**31, -NUM) if negative else min(2**31-1, NUM)




