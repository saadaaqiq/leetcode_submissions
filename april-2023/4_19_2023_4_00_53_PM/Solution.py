# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        for j in range(len(digits)-1, -1, -1):
            x = digits[j] + (1 if j == len(digits)-1 else 0) + c
            digits[j], c = x % 10, x // 10
        return ([c] if c else []) + digits
