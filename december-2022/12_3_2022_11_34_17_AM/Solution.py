# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array

class Solution:
    def isMajorityElement(self, A: List[int], t: int) -> bool:
        return True if bisect_right(A,t) - bisect_left(A,t) > len(A)/2 else False
