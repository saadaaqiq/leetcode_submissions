# https://leetcode.com/problems/print-immutable-linked-list-in-reverse

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
  def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    c = 0
    realHead = head
    while head:
      c += 1
      head = head.getNext()
    head = realHead
    while c > 0:
      for i in range(0,c-1):
        head = head.getNext()
      head.printValue()
      head = realHead
      c -= 1
    