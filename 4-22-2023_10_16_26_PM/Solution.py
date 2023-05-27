# https://leetcode.com/problems/jump-game-vii

class Solution:
    def canReach(self, s: str, mij: int, maj: int) -> bool:
        n = len(s)
        if n == 1: return True
        if s[-1] != '0': return False
        t = [i for (i,c) in enumerate(s) if c == '0']
        t.reverse()
        z = []
        while t:
            if not z or z[-1][1] != t[-1] - 1:
                z.append([t[-1], t[-1]])
            else:
                z[-1][1] = t[-1]
            t.pop()
        z.reverse()
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
            
        
        