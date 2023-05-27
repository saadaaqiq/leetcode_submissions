# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs

class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    leafAncestors = []
    c = 0
    
    def distanceCalculator(leafAnc1, leafAnc2):
      d = 2
      q1, q2 = deque(leafAnc1), deque(leafAnc2)
      while q1 and q2:
        a,b = q1.popleft(), q2.popleft()
        if a == b:
          continue
        else:
          d += 2
          break
      return d + len(q1) + len(q2)
    
    def dfs(node, ancestors):
      if node.left:
        dfs(node.left, ancestors + [node])
      if node.right:
        dfs(node.right, ancestors + [node])
      if not node.left and not node.right:
        leafAncestors.append(ancestors)
    
    dfs(root, [])
    
    for i in range(len(leafAncestors)):
      for j in range(i, len(leafAncestors)):
        if i != j and distanceCalculator(leafAncestors[i],leafAncestors[j]) <= distance:
          c += 1
    
    return c
        
      