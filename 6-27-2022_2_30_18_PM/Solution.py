# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
    pointedAtBy = {}
    oldToNew = {}
    
    node = head
    
    newNode = Node(-1)
    newHead = newNode
    
    while node:
      
      newNode.next = Node(node.val)
      newNode = newNode.next
      
      oldToNew[node] = newNode
      
      if node in pointedAtBy:
        for pointingNode in pointedAtBy[node]:
          oldToNew[pointingNode].random = newNode
          
      if node.random:
        if node.random not in pointedAtBy:
          pointedAtBy[node.random] = []
        pointedAtBy[node.random].append(node)
        if node.random in oldToNew:
          newNode.random = oldToNew[node.random]
          
      node = node.next
    
    return newHead.next
      
    