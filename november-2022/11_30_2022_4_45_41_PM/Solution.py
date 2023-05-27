# https://leetcode.com/problems/find-the-distance-value-between-two-arrays

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = len(arr1)
        for num in arr1:
            l, r = 0, len(arr2)
            while l < r:
                mid = (l+r)//2
                if abs(num-arr2[mid]) <= d:
                    res -= 1
                    break
                else:
                    if num - arr2[mid] >= 0: l = mid + 1
                    else: r = mid
        return res


