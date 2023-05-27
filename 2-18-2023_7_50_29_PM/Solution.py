# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [c for c in str(num)]
        arr.sort()
        return int(arr[0] + arr[2]) + int(arr[1] + arr[3])