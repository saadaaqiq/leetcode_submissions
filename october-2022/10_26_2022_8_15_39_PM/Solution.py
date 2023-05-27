# https://leetcode.com/problems/my-calendar-i

class TreeNode:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.left = None
    self.right = None

class MyCalendar:
  def __init__(self):
    self.root = TreeNode(-1,-1)

  def book(self, start: int, end: int) -> bool:
    return self.dfs(start, end, self.root)
  
  def dfs(self, start, end, node):
    if node.start == -1 and node.end == -1:
      node.start = start
      node.end = end
      return True
    if (node.start <= start and start < node.end) or (node.start < end and end <= node.end):
      return False      
    if node.end <= start :
      if not node.right:
        node.right = TreeNode(start, end)
        return True
      else:
        return self.dfs(start, end, node.right)
    if end <= node.start:
      if not node.left:
        node.left = TreeNode(start, end)
        return True
      else:
        return self.dfs(start, end, node.left)
    return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)