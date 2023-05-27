# https://leetcode.com/problems/lru-cache

class LRUCache: 

    def __init__(self, capacity: int):
        self.n = capacity
        self.dic = {}
        self.order = -1
        self.ord_dic = {}
        self.last_used = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            self.order += 1
            self.last_used[key] = self.order
            self.ord_dic[self.order] = key
            self.q.append(self.order)
            return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if len(self.dic) >= self.n and key not in self.dic:
            while self.q:
                last = self.q.popleft()
                x = self.ord_dic[last]
                if x in self.dic and x in self.last_used and self.last_used[x] == last:
                    del self.dic[x]
                    break
                elif x in self.dic and x in self.last_used and self.last_used[x] != last:
                    del self.ord_dic[last]
        self.dic[key] = value
        y = self.get(key)
