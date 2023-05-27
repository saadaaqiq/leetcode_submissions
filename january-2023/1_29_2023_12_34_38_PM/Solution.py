# https://leetcode.com/problems/data-stream-as-disjoint-intervals

class SummaryRanges:

    def __init__(self):
        self.par =  collections.defaultdict(int)
        self.rank = collections.defaultdict(int)

    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i, j):
        x, y = self.find(i), self.find(j)
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            self.rank[x] += 1

    def addNum(self, k: int) -> None:
        if k in self.par:
            return 
        self.par[k] = k
        if k-1 in self.par:
            self.union(k-1, k)
        if k+1 in self.par:
            self.union(k+1, k)
        
    def getIntervals(self) -> List[List[int]]:
        for i in self.par:
            self.find(i)
        arr = []
        for p in set(self.par.values()):
            print(p)
            x, y = p, p
            while x-1 in self.par:
                x -= 1
            while y+1 in self.par:
                y += 1
            arr.append([x, y])
        return sorted(arr)
            
        






# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()