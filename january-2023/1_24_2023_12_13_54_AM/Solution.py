# https://leetcode.com/problems/reverse-linked-list

class Solution:
  def reverseList(self, head):
    cur = head
    prev = None
    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur 
      if not nxt: 
        return cur
      cur = nxt
    return cur
