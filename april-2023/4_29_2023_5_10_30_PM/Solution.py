# https://leetcode.com/problems/flatten-nested-list-iterator

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        def dfs(x):
            if x.isInteger():
                self.stack.append(x.getInteger())
            else:
                for y in reversed(x.getList()):
                    dfs(y)
        for y in reversed(nestedList):
            dfs(y)
        

    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())