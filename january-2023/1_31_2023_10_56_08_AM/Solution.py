# https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], t: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0][0] == t[0] and triplets[0][1] == t[1] and triplets[0][2] == t[2]
        b1, b2, b3 = False, False, False        
        for x,y,z in triplets:
            if x == t[0] and y <= t[1] and z <= t[2]:
                b1 = True
                break
        for x,y,z in triplets:    
            if y == t[1] and x <= t[0] and z <= t[2]:
                b2 = True
                break
        for x,y,z in triplets:
            if z == t[2] and x <= t[0] and y <= t[1]:
                b3 = True
                break
        return b1 and b2 and b3