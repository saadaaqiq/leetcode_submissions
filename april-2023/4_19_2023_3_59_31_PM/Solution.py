# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 0
        for j in range(n-1, -1, -1):
            digits[j], c = (digits[j] + (1 if j == n-1 else 0) + c) % 10, (digits[j] + (1 if j == n-1 else 0) + c) // 10
        if c == 0:
            return digits
        else:
            return [c] + digits
