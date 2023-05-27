# https://leetcode.com/problems/linked-list-random-node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.l = 0
        cur = head
        while cur:
            self.l += 1
            cur = cur.next

    def getRandom(self) -> int:
        r = random.randrange(0, self.l)
        cur = self.head
        i = 0 
        while i < r:
            cur = cur.next
            i += 1
        return cur.val 

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()