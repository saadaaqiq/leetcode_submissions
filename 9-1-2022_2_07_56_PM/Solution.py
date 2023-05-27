# https://leetcode.com/problems/count-good-nodes-in-binary-tree

class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, maxi):
      if not node: return 0
      c = 1 if node.val >= maxi else 0
      return c + dfs(node.right, max(maxi, node.val)) + dfs(node.left, max(maxi, node.val))
    return  dfs(root, -10001)
