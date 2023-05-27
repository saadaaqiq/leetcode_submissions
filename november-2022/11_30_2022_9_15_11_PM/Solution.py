# https://leetcode.com/problems/fixed-point

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = bisect_left(arr, 0), bisect_right(arr, len(arr)-1)
        for i in range(l,r):
            if arr[i] == i:
                return i
        return -1