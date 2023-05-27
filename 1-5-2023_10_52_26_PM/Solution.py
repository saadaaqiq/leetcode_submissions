# https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(a, b):
            if not a: return b
            if not b: return a
            if a.val <= b.val:
                a.next = merge(a.next, b)
                return a
            else:
                b.next = merge(a, b.next)
                return b
        
        def split(root):
            if not root or not root.next:
                return root
            slow, fast = root, root
            pre = ListNode(0)
            pre.next = root
            while fast and fast.next:
                pre, slow, fast = pre.next, slow.next, fast.next.next
            pre.next = None
            return merge(split(root), split(slow))

        return split(head)



                    

            