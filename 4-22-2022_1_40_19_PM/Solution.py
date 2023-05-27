# https://leetcode.com/problems/reorder-list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list = []
        curr = head
        while curr:
            list.append(curr)
            curr = curr.next
        i = 0
        j = len(list) - 1
        while i<j-1:
            list[i].next = list[j]
            i+=1
            list[j].next = list[i]
            j-=1
            list[j].next = None
        return head