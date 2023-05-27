# https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = [dist[i]/speed[i] for i in range(len(dist))]
        arr.sort()
        ts = 0
        for t in arr:
            if t <= ts:
                return ts
            else:
                ts += 1
        return ts