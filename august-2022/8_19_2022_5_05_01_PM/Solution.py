# https://leetcode.com/problems/intersection-of-three-sorted-arrays

class Solution:
  def arraysIntersection(self, arr1, arr2, arr3):
    return sorted(set(arr1).intersection(set(arr2)).intersection(set(arr3)))
      