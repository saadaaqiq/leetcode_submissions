# https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def closer(a, b):
            if abs(a-x) < abs(b-x):
                return -1
            elif abs(a-x) > abs(b-x):
                return 1
            else:
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0
        
        return sorted(sorted(arr, key= functools.cmp_to_key(closer))[:k])