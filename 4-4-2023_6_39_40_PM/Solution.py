# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        for i in range(len(dp)-1, -1, -1):
            for word in wordDict:
                if len(word) + i <= len(s) and s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
                    break
        return dp[0]