# https://leetcode.com/problems/path-sum-iii

class Solution:
  def pathSum(self, root: Optional[TreeNode], target: int) -> int:
    if not root:
      return 0
    prefixSums = {0:1}
    res = 0
    def dfs(node, s):
      nonlocal res
      somme = s + node.val
      if somme - target in prefixSums:
        res += prefixSums[somme-target]
      if somme not in prefixSums:
        prefixSums[somme] = 0
      prefixSums[somme] += 1
      if node.left:
        dfs(node.left, somme)
      if node.right:
        dfs(node.right, somme)
      prefixSums[somme] -= 1
    dfs(root, 0)
    return res
