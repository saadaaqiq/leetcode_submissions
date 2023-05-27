# https://leetcode.com/problems/valid-square

class Solution:
    def validSquare(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> bool:
        
        def dist(a, b):
            return sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2)

        x1, x2, x3 = dist(A,B), dist(A,C), dist(A,D)
        y2, y3 = dist(B,C), dist(B,D)
        z3 = dist(C,D)

        Am, AM = min(x1,x2,x3), max(x1,x2,x3)
        Bm, BM = min(x1, y2, y3), max(x1, y2, y3)
        Cm, CM = min(x2, y2, z3), max(x2, y2, z3)
        Dm, DM = min(x3, y3, z3), max(x3, y3, z3)

        if not (Am == Bm == Cm == Dm) or AM==0 or BM==0 or CM==0 or DM==0: 
            return False
        
        if Counter([x1,x2,x3])[Am] != 2 or Counter([x1, y2, y3])[Bm] != 2 or Counter([x2, y2, z3])[Cm] != 2 or Counter([x3, y3, z3])[Dm] != 2:
            return False 

        if not (Am/AM == Bm/BM == Cm/CM == Dm/DM):
            return False

        return True

        
        
        
