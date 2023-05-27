# https://leetcode.com/problems/largest-bst-subtree

class Solution:
  def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    
    if not root:
      return 0
    
    m=0
    
    def postorder(node):
      nonlocal m
      if not node.left and not node.right:
        m = max(1, m)
        return node.val, node.val, 1, True
      size, nmin, nmax = 1, 10001, -10001
      lg = True if not node.left else False
      rg = True if not node.right else False
      if node.left:
        lmin, lmax, lsize, b = postorder(node.left)
        nmin, nmax = min(nmin, lmin), max(nmax, lmax)
        if b and lmax < node.val and node.left.val < node.val:
          size += lsize
          lg = True
      if node.right:
        rmin, rmax, rsize, b = postorder(node.right)
        nmin, nmax = min(nmin, rmin), max(nmax, rmax)
        if b and rmin > node.val and node.right.val > node.val:
          size += rsize
          rg = True
      if lg and rg:
        m = max(size, m)
      return nmin, nmax, size, lg and rg
      
    postorder(root)
    return m
    
    
      
          
      
          