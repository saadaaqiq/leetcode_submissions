# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n < 3:
            return arr[n]
        while len(arr) <= n:
            arr.append(arr[-1] + arr[-2] + arr[-3])
        print(arr)
        return arr[-1]