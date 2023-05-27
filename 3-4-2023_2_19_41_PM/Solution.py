# https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0
        while i < n:
            j = 1
            while i + j < n and chars[i + j] == chars[i]:
                j += 1
            chars[k] = chars[i]
            k += 1
            if j > 1:
                for c in str(j):
                    chars[k] = c
                    k += 1
            i = i + j
        return k