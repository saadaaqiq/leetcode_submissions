# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr = [0] * 26
        for c in word1:
            arr[ord(c)-97] += 1
        for c in word2:
            arr[ord(c)-97] -= 1
        return -3 <= min(arr) <= max(arr) <= 3