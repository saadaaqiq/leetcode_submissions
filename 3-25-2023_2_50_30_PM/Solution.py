# https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, arr: List[int], k: int) -> bool:
        n, i, planted = len(arr), 0, 0
        while i < n:
            if arr[i] != 0:
                i += 1 
            else:
                c = 0 if i > 0 else 1
                while i < n and arr[i] == 0:
                    i += 1
                    c += 1 if i < n else 2
                planted += math.ceil(c / 2) - 1
                
        return planted >= k