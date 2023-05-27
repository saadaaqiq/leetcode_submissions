# https://leetcode.com/problems/shuffle-an-array

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.arr.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
