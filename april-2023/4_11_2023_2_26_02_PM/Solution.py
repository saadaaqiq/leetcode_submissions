# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        x, y = l1, l2
        carry = 0
        before_head = ListNode()
        cur = before_head
        while x and y:
            cur.next = ListNode((x.val + y.val + carry)%10)
            carry = (x.val + y.val + carry)//10
            cur = cur.next
            x = x.next
            y = y.next
        a = x if x else y
        while a:
            cur.next = ListNode((a.val + carry) % 10)
            carry = (a.val + carry)//10
            a = a.next
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        return before_head.next
