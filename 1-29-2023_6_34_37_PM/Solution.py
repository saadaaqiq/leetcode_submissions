# https://leetcode.com/problems/concatenated-words

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        dp = {}

        def is_concat(s):
            if s in dp:
                return dp[s]
            for i in range(1, len(s)):
                if s[:i] in word_set and (s[i:] in word_set or is_concat(s[i:])):
                    dp[s] = True
                    return True
            dp[s] = False
            return False

        res = []

        for w in words:
            if is_concat(w):
                res.append(w)

        return res



        

