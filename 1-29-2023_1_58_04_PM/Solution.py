# https://leetcode.com/problems/data-stream-as-disjoint-intervals

from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.dic = SortedDict()

    def addNum(self, k: int) -> None:
        if k in self.dic:
            return
        self.dic[k] = k
        ind = self.dic.index(k)
        px, py, nx, ny = k, k, k, k
        if ind-1>=0:
            px, py = self.dic.peekitem(ind-1)
            if py >= k:
                self.dic.pop(k)
                return
        if ind+1<len(self.dic):
            nx, ny = self.dic.peekitem(ind+1)
            if nx <= k:
                self.dic.pop(k)
                return
        if py == k-1 and not (nx == k + 1):
            self.dic[px] = k
            self.dic.pop(k)
        elif nx == k + 1 and not (py == k-1):
            self.dic[k] = ny
            self.dic.pop(k+1)
        elif py == k-1 and nx == k + 1:
            self.dic[px] = ny
            self.dic.pop(k+1)
            self.dic.pop(k)
 
    def getIntervals(self) -> List[List[int]]:
        arr = []
        for x, y in self.dic.items():
            arr.append([x,y])
        print(self.dic)
        return arr
        






# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()