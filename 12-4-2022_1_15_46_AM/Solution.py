# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k

class Solution:
    def findMinFibonacciNumbers(self, target: int) -> int:
        arr = [1, 1]
        while arr[-1] < 1000000001:
            arr.append(arr[-1]+arr[-2])
        n = len(arr)
        res = 0
        for i in range(n-1, -1, -1):
            while target - arr[i] >= 0:
                res += 1
                target -= arr[i]
        return res
            