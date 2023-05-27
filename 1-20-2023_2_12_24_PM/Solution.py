# https://leetcode.com/problems/distribute-candies

class Solution:
    def distributeCandies(self, arr: List[int]):
        return min(len(set(arr)), len(arr)//2)
            