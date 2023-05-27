# https://leetcode.com/problems/validate-binary-search-tree

class Solution:

  def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def validator(node, inter):
      mini, maxi = inter[0], inter[1]
      if not node:
        return True
      if not (node.val < inter[1] and node.val > inter[0]):
        return False
      if not validator(node.left, [mini,node.val]):
        return False
      if not validator(node.right, [node.val, maxi]):
        return False
      return True

    return validator(root, [-sys.maxsize,sys.maxsize])