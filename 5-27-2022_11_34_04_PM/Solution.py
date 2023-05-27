# https://leetcode.com/problems/combination-sum-iv

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.next = {}
class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    visited = { 0:1 }
    def dfs(node):
      if node.val in visited:
        return visited[node.val]
      for num in nums:
        if node.val >= num:
          node.next[node.val-num] = TreeNode(node.val-num)
      res = 0
      for k in node.next:
        res += dfs(node.next[k])
      visited[node.val] = res
      return res
    return dfs(TreeNode(target))