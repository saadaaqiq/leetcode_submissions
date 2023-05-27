# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if 0 <= ord(c) - 97 < 26 or c.isnumeric():
                arr.append(c)
            elif 0 <= ord(c) - 65 < 26:
                arr.append(chr(ord(c) - 65 + 97))
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
            