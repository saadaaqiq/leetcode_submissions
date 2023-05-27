# https://leetcode.com/problems/intersection-of-three-sorted-arrays

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return list(sorted(set(arr1).intersection(set(arr2).intersection(set(arr3)))))







            
        
        
