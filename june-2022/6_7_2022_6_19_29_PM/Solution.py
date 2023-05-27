# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    paths=[]
    c=0
    def dfs(node,path):
      if node.right or node.left:
        if node.right:
          dfs(node.right, path+[True])
        if node.left:
          dfs(node.left, path+[False])
      else:
        paths.append(path)
    dfs(root,[])
    for i in range(len(paths)-1):
      for j in range(i+1,len(paths)):
        d = 0
        k=0
        p=paths[i]
        q=paths[j]
        l1=len(p)
        l2=len(q)
        while k<min(l1,l2) and p[k]==q[k]:
          k+=1
        if k==l1 and k!=l2:
          d+=l2-k
        elif k==l2 and k!=l1:
          d+=l1-k
        else:
          d+=l1+l2-2*k
        if d <= distance:
          c+=1
    return c
          
          
    