# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted([(num, i) for (i, num) in enumerate(nums)])
        res = [0] * len(nums)
        while arr:
            x, i = arr.pop()
            indexes = [i]
            while arr and arr[-1][0] == x:
                indexes.append(arr.pop()[1])
            for k in indexes:
                res[k] = len(arr)
        return res
