# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, arr: List[str]) -> bool:
        
        @cache 
        def dfs(i):
            if i == len(s):
                return True
            for w in arr:
                if i + len(w) <= len(s) and w == s[i:i+len(w)] and dfs(i + len(w)):
                        return True
            return False
        
        return dfs(0)
            
