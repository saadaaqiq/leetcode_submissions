# https://leetcode.com/problems/maximum-frequency-stack

class FreqStack:

    def __init__(self):
        self.mc = 0
        self.d1 = collections.defaultdict(int)
        self.d2 = collections.defaultdict(list)


    def push(self, v: int) -> None:
        self.d1[v] += 1
        self.mc = max(self.mc, self.d1[v])
        self.d2[self.d1[v]].append(v)
        
    def pop(self) -> int:
        v = self.d2[self.mc].pop()
        self.d1[v] -= 1
        if not self.d2[self.mc]:
            self.mc -= 1
        return v

