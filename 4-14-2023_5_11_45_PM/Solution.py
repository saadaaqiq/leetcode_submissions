# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, arr):
        n = len(arr)
        counter = collections.Counter(arr)
        nums = []
        res = set()
        if counter[0] > 2:
            res.add((0, 0, 0))
        for x in counter:
            for j in range(min(counter[x], 2)):
                nums.append(x)
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
        
        for i in range(n-1):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]
                if - x - y in dic:
                    for k in dic[-x-y]:
                        if i!=k and j!=k:
                            z = -x-y
                            res.add(tuple(sorted([x, y, z])))
        return res