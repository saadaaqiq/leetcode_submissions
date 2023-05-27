# https://leetcode.com/problems/sort-list

class Solution:
    def sortList(self, head):
        # merges two sorted lists
        # returns: new head and tail of merged list
        def merge(first, second):
            head = tail = None
            while first or second:
                if not first or second and first.val > second.val:
                    first, second = second, first
                if head:
                    tail.next = first
                else:
                    head = first
                tail, first = first, first.next
            return head, tail

        # splits list of first n nodes
        # returns: next node after the split list
        def split(head, n):
            if not head or n == 0:
                return None
            while n > 1 and head.next:
                head, n = head.next, n-1
            head.next, head = None, head.next
            return head

        # splits two lists of first n+n nodes, merges them
        # returns: new head and tail of merged list, and next node after
        def merge_pair(first, n):
            second = split(first, n)
            next_pair = split(second, n)
            return *merge(first, second), next_pair

        # repetitively merges list pairs of n+n nodes
        # returns: new head of list, and second pair (if any)
        def merge_pairs(head, n):
            head, tail, next_pair = _, _, second_pair = merge_pair(head, n)
            while next_pair:
                tail.next, tail, next_pair = merge_pair(next_pair, n)
            return head, second_pair

        n, second_pair = 1, True
        while second_pair:
            head, second_pair = merge_pairs(head, n)
            n *= 2
            
        return head