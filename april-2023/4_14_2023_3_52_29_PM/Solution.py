# https://leetcode.com/problems/lru-cache

class LinkNode:
    def __init__(self, key=-1, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.k = 0
        self.dic = {}
        self.head = LinkNode(-1, -1)
        self.tail = LinkNode(-2, -2)
        self.head.right = self.tail
        self.tail.left = self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            node.left.right, node.right.left = node.right, node.left
            node.left, node.right = self.tail.left, self.tail
            self.tail.left.right, self.tail.left = node, node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            self.dic[key] = LinkNode(key, value, self.tail.left, self.tail)
            self.tail.left.right, self.tail.left = self.dic[key], self.dic[key]
            self.k += 1
            if self.k > self.n:
                self.k -= 1
                del self.dic[self.head.right.key]
                self.head.right.right.left, self.head.right = self.head, self.head.right.right
        else:
            self.dic[key].val = value
            self.get(key)














# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)