# https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, arr: List[List[int]]) -> int:
        res = len(arr)
        arr.sort(key=lambda x:(x[0],-x[1]))
        i, j = 0, 1
        while j < len(arr):
            if arr[i][0] <= arr[j][0] and arr[j][1] <= arr[i][1]:
                res -= 1
            else:
                i = j
            j += 1
        return res
