# https://leetcode.com/problems/wiggle-sort

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        h1, h2 = [], []
        for i,num in enumerate(nums):
            heapq.heappush(h1, (num,i))
            heapq.heappush(h2, (-num,i))
        i = 0
        vis = set()
        b = False
        while i < len(nums):
            if not b:
                while h1[0][1] in vis:
                    heapq.heappop(h1)
                nums[i], v = heapq.heappop(h1)
                vis.add(v)
                b = True 
            else:
                while h2[0][1] in vis:
                    heapq.heappop(h2)
                p, v = heapq.heappop(h2)
                nums[i] = -p
                vis.add(v)
                b = False
            i+=1