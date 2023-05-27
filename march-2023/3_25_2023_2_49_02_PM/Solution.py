# https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, arr: List[int], k: int) -> bool:
        res = 0
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] != 0:
                i += 1 
            else:
                c = 0
                if i == 0:
                    c += 1
                while i < n and arr[i] == 0:
                    if i == n-1:
                        c += 1
                    i += 1
                    c += 1
                res += math.ceil(c / 2) - 1
                
        return res >= k