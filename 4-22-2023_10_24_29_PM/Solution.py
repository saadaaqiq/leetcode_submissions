# https://leetcode.com/problems/jump-game-vii

class Solution:
    def canReach(self, s: str, mij: int, maj: int) -> bool:
        n = len(s)
        if n == 1: 
            return True
        if s[-1] != '0': 
            return False
        z = []
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                if not z or z[-1][0] - 1 > i:
                    z.append([i,i])
                else:
                    z[-1][0] -= 1
        x, y = 0, 0
        while z:
            l, r = z[-1]
            if y + maj < l:
                return False
            elif x + mij > r:
                z.pop()
            else:
                x, y = max(x + mij, l), min(y + maj, r)
        return x <= n-1 <= y
            
        
        