# https://leetcode.com/problems/lru-cache

class LRUCache: 

    def __init__(self, capacity: int):
        self.n = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.n == len(self.dic) and key not in self.dic:
            self.dic.popitem(False)
        self.dic[key] = value
        self.dic.move_to_end(key)