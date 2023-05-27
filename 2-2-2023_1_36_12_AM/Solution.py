# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, arr: List[str]) -> bool:
        word_set = set(arr)

        @cache
        def dfs(i):
            if i == len(s):
                return True
            for j in range(len(s)+1):
                if s[i:j] in word_set:
                    if dfs(j):
                        return True
            return False

        return dfs(0)