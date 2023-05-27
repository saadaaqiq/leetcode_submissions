# https://leetcode.com/problems/linked-list-random-node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.arr = []
        cur = head
        while cur:
            self.arr.append(cur)
            cur = cur.next

    def getRandom(self) -> int:
        r = random.randrange(0, len(self.arr))
        return self.arr[r].val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()