# https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        diff = inf
        for i in range(n-1):
            diff = min(diff, arr[i+1] - arr[i])
        res = []
        for i in range(n-1):
            j = i+1
            while j < n and arr[j] - arr[i] == diff:
                res.append([arr[i], arr[j]])
                j += 1
        return res