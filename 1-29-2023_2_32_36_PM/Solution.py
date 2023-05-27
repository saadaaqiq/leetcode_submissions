# https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        curr = []
        res = []

        def dfs(l, r):
            if l == r:
                res.append(curr.copy())
                return
            for i in range(l, r):
                if is_pal(l, i):
                    curr.append(s[l:i+1])
                    dfs(i+1, r)
                    curr.pop()
            return 

        dfs(0, len(s))
        
        return res




            
            
            