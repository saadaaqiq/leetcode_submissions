# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree

class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    stack = []
    mini = 0
    for num in preorder:
      if num < mini: return False
      while stack and stack[-1] < num: mini = stack.pop()
      stack.append(num)
    return True