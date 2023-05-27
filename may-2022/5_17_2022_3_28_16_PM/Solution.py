# https://leetcode.com/problems/validate-binary-search-tree

class Solution:

  def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def validator(node, mini, maxi):
      return (not node or (node.val<maxi and node.val>mini and validator(node.left,mini,node.val) and validator(node.right,node.val,maxi)))

    return validator(root, -sys.maxsize, sys.maxsize)