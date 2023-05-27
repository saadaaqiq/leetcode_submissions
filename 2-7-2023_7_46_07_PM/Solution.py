# https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, A: List[int]) -> int:
        x, xc, y, yc = -1, 0, -1, 0
        c, r = 0, 0
        for i, a in enumerate(A):
            if x == -1:
                x = a
                xc += 1
            elif y == -1:
                if x == a:
                    xc += 1
                else:
                    y = a 
                    yc += 1
            else:
                if a == y:
                    yc += 1
                elif a == x:
                    x, xc, y, yc = y, yc, x, 1
                else:
                    x, xc, y, yc = y, yc, a, 1
                    r = max(r, c)
                    c = xc + yc - 1
            c += 1
            
        return max(r, c)








            









