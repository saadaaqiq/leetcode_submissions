# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = [[]]
        for x in nums:
            if x == 0:
                arr.append([])
            else:
                arr[-1].append(x)
        res = - math.inf
        if len(arr) > 1:
            res = 0
        for tab in arr:
            if not tab:
                continue
            p = math.prod(tab)
            if p > 0 or len(tab) == 1:
                res = max(res, p)
                continue
            y, z = p, p
            for i in range(len(tab)):
                y //= tab[i]
                if tab[i] < 0:
                    break
            for i in range(len(tab)-1, -1, -1):
                z //= tab[i]
                if tab[i] < 0:
                    break
            res = max(res, y, z)
        return res
                                    
            