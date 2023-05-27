# https://leetcode.com/problems/valid-square

class Solution:
    def validSquare(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> bool:
        
        def dist(a, b):
            return sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2)

        x1, x2, x3 = dist(A,B), dist(A,C), dist(A,D)
        y1, y2, y3 = dist(B,A), dist(B,C), dist(B,D)
        z1, z2, z3 = dist(C,A), dist(C,B), dist(C,D)
        t1, t2, t3 = dist(D,A), dist(D,B), dist(D,C)

        Am, AM = min(x1,x2,x3), max(x1,x2,x3)
        Bm, BM = min(y1, y2, y3), max(y1, y2, y3)
        Cm, CM = min(z1, z2, z3), max(z1, z2, z3)
        Dm, DM = min(t1, t2, t3), max(t1, t2, t3)

        if not (Am == Bm == Cm == Dm) or AM==0 or BM==0 or CM==0 or DM==0: 
            return False
        
        if Counter([x1, x2, x3])[Am] != 2 or Counter([y1, y2, y3])[Bm] != 2 or Counter([z1, z2, z3])[Cm] != 2 or Counter([t1, t2, t3])[Dm] != 2:
            return False 

        if not (Am/AM == Bm/BM == Cm/CM == Dm/DM):
            return False

        return True

        
        
        
