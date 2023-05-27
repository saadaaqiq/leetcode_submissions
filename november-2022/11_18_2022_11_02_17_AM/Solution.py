# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        for n in nums:
            if not arr or n > arr[-1][-1] + 1:
                arr.append([n])
            else:
                arr[-1].append(n)
        for i, inter in enumerate(arr):
            if len(inter)==1:
                arr[i] = str(inter[0])
            else:
                arr[i] = str(inter[0]) + "->" + str(inter[-1])
        return arr
