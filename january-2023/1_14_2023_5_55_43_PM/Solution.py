# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = -math.inf
        arr = [[]]

        for num in nums:
            if num != 0:
                arr[-1].append(num)
            else:
                res = 0
                arr.append([])
        
        for tab in arr:
            if not tab:
                continue
            P = math.prod(tab)
            if P >= 0:
                res = max(res, P)
            else:
                if len(tab) == 1:
                    res = max(res, tab[0])
                else:
                    first_neg_ind, last_neg_ind = -1, -1
                    for k, x in enumerate(tab):
                        if x < 0:
                            first_neg_ind = k
                            break
                    for k in range(len(tab)-1, -1, -1):
                        if tab[k] < 0:
                            last_neg_ind = k
                            break
                    res = max(res, math.prod(tab[:last_neg_ind]), math.prod(tab[first_neg_ind+1:]))
        return res
