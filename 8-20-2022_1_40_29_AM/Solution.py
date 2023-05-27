# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Codec:
  def encode(self, root):
    if not root:
      return None
    q = deque()
    biroot = TreeNode(root.val)
    q.append((root, biroot))
    while q:
      node, binode = q.popleft()
      for i, child in enumerate(node.children):
        bichild = TreeNode(child.val)
        if i == 0:
          binode.right = bichild
          binode = binode.right
        else:
          binode.left = bichild
          binode = binode.left
        q.append((child, binode))
    return biroot

  def decode(self, biroot):
    if not biroot:
      return None
    stack = []
    root = Node(biroot.val, [])
    root_parent = None
    stack.append((biroot, root, root_parent))
    while stack:
      binode, node, parent = stack.pop()
      if binode.right:
        child = Node(binode.right.val, [])
        node.children.append(child)
        stack.append((binode.right, child, node))
      if binode.left:
        sibling = Node(binode.left.val, [])
        parent.children.append(sibling)
        stack.append((binode.left, sibling, parent))
    return root

