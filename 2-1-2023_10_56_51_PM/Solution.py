# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, arr: List[str]) -> bool:
        
        lead_nowhere = set() 

        def dfs(i):
            if i in lead_nowhere:
                return False
            if i == len(s):
                return True
            for w in arr:
                if i + len(w) <= len(s) and w == s[i:i+len(w)] and dfs(i + len(w)):
                    return True
            lead_nowhere.add(i)
            return False
        
        return dfs(0)
            
