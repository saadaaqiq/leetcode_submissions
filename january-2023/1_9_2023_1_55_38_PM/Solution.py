# https://leetcode.com/problems/lru-cache

class DLL:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache: 

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.head, self.tail = DLL(), DLL()
        self.head.next, self.tail.prev = self.tail, self.head

    def put(self, key: int, value: int) -> None:
        if len(self.dic) == self.cap:
            if key in self.dic:
                node = self.dic[key]
                node.val = value
                self.remove_node(node)
                self.put_node_last(node)
            else:
                lru = self.get_lru()
                del self.dic[lru.key]
                self.remove_node(lru)
                node = DLL(key, value)
                self.put_node_last(node)
                self.dic[key] = node
        else:
            if key in self.dic:
                node = self.dic[key]
                node.val = value
                self.remove_node(node)
                self.put_node_last(node)
            else:
                node = DLL(key, value)
                self.put_node_last(node)
                self.dic[key] = node


    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove_node(node)
            self.put_node_last(node)
            return node.val
        return -1
        

    def get_lru(self) -> DLL:
        return self.head.next

    def remove_node(self, node) -> None:
        P, N = node.prev, node.next
        P.next, N.prev = N, P

    def put_node_last(self, node) -> None:
        P, N = self.tail.prev, self.tail
        P.next, N.prev = node, node
        node.prev, node.next = P, N



            