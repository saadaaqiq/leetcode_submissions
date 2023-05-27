# https://leetcode.com/problems/maximum-frequency-stack

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class FreqStack:

    def __init__(self):
        self.count_to_node = {}
        self.val_to_count = collections.defaultdict(int)
        self.max_count = 0

    def push(self, val: int) -> None:
        node = ListNode(val)
        self.val_to_count[val] += 1
        new_count = self.val_to_count[val]
        self.max_count = max(self.max_count, new_count)
        if new_count in self.count_to_node:
            node.next = self.count_to_node[new_count]
        self.count_to_node[new_count] = node
        
    def pop(self) -> int:
        node = self.count_to_node[self.max_count]
        self.val_to_count[node.val] -= 1
        if not node.next:
            del self.count_to_node[self.max_count]
            self.max_count -= 1
        else:
            self.count_to_node[self.max_count] = node.next
        return node.val

