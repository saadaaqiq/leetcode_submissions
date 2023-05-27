# https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(list(zip(*heapq.nsmallest(k, enumerate(arr), key=lambda tup: (abs(tup[1]-x), tup[0]))))[1])
