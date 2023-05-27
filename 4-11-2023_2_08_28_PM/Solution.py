# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        # the trick here is to realize that a = b means a ^ b = 0
        res = 0
        for i in range(n-1):
            cur = arr[i]
            for k in range(i+1, n):
                cur ^= arr[k]
                if cur == 0:
                    res += k - i
        return res