# https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = target
        if len(triplets) == 1:
            return triplets[0][0] == a and triplets[0][1] == b and triplets[0][2] == c
        b1, b2, b3 = False, False, False        
        for x,y,z in triplets:
            if x == a and y <= b and z <= c:
                b1 = True
            if y == b and x <= a and z <= c:
                b2 = True
            if z == c and x <= a and y <= b:
                b3 = True
        return b1 and b2 and b3