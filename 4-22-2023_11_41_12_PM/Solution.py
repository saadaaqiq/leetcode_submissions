# https://leetcode.com/problems/operations-on-tree

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [0] * len(parent)
        self.adj = {i: [] for i in range(len(parent))}
        for i, p in enumerate(parent):
            if p >= 0:
                self.adj[p].append(i)
         
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == 0:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        cur = num
        while cur >= 0:
            if self.locked[cur] > 0:
                return False
            cur = self.parent[cur]
        locked_descendants = []
        stack = [num]
        while stack:
            x = stack.pop()
            if self.locked[x] > 0:
                locked_descendants.append(x)
            for y in self.adj[x]:
                stack.append(y)
        if not locked_descendants:
            return False
        for ld in locked_descendants:
            self.locked[ld] = 0
        self.locked[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)