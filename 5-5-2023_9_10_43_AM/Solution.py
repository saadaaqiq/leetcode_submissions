# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = Counter(s[:k])
        vowels = set(['a','e','i','o','u'])
        cur = sum([count[v] for v in vowels])
        res = cur
        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i-k] in vowels:
                cur -= 1
            res = max(res, cur)
        return res