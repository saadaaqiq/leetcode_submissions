# https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        A = set()
        curr = [0] * 21

        def backtrack(i):
            if i == len(nums):
                A.add(tuple(curr))
                return 
            # include i
            curr[nums[i] + 10] += 1
            backtrack(i+1)
            curr[nums[i] + 10] -= 1 
            # don't include i
            backtrack(i+1)
            return 

        backtrack(0)

        def transformer(arr):
            X = []
            for i in range(len(arr)):
                for j in range(arr[i]):
                    X.append(i-10)
            return X

        res = []
        for a in A:
            res.append(transformer(a))

        return res