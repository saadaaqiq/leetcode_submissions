# https://leetcode.com/problems/fixed-point

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid] >= mid:
                r = mid
            else:
                l = mid + 1
        return l if 0 <= l < len(arr) and arr[l] == l else -1

            
        