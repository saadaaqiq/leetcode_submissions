# https://leetcode.com/problems/sort-list

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        curr = head
        k = 0
        while curr:
            arr.append((curr.val, k, curr))
            k += 1
            curr = curr.next
        arr.sort()
        res = arr[0][2]
        for i in range(len(arr)):
            arr[i][2].next = arr[i+1][2] if i < len(arr)-1 else None
        return res
            
            