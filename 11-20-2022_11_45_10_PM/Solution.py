# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def rotate(arr):
            A = []
            for i in range(len(arr)):
                temp = arr.copy()
                A.append(temp[i:] + temp[:i])
            return A
                
        def perm(arr):
            A = []
            if len(arr)==1: return [arr]
            if len(arr)==2: return [[arr[0],arr[1]], [arr[1],arr[0]]]
            for rot in rotate(arr):
                for P in perm(rot[1:]):
                    A.append([rot[0]] + P)
            return A
        
        return perm(nums)

            