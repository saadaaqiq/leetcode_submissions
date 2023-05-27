# https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        res = []
        for i, n in enumerate(arr):
            heapq.heappush(h, (abs(x-n), i))
        for i in range(k):
            res.append(arr[heapq.heappop(h)[1]])
        return sorted(res)