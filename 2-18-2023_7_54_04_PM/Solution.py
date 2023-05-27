# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        r = num
        for i in range(3, -1, -1):
            q, r = r // (10**i), r % (10**i)
            arr.append(q)
        arr.sort()
        return arr[0] * 10 + arr[2] + arr[1] * 10 + arr[3]
