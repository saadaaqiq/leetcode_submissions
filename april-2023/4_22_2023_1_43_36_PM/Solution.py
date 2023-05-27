# https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        X = [1] * n
        Y = [1] * n

        for i in range(n-2, -1, -1):
            if (i % 2 == 1 and arr[i] > arr[i+1]) or (i % 2 == 0 and arr[i] < arr[i+1]):
                X[i] += X[i+1]
            if (i % 2 == 0 and arr[i] > arr[i+1]) or (i % 2 == 1 and arr[i] < arr[i+1]):
                Y[i] += Y[i+1]
        return max(max(X), max(Y))