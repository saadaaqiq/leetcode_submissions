# https://leetcode.com/problems/data-stream-as-disjoint-intervals

class TreeNode:
    def __init__(self, v=-1):
        self.val = v
        self.left = None
        self.right = None

class SummaryRanges:

    def __init__(self):
        self.root = TreeNode()

    def addNum(self, k: int) -> None:
        curr = self.root
        while curr:
            if k > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(k)
                    break
            elif k < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(k)
                    break
            else:
                break

    def getIntervals(self) -> List[List[int]]:
        arr = []

        def dfs(node):
            if node.left: dfs(node.left)
            arr.append(node.val)
            if node.right: dfs(node.right)   
        
        dfs(self.root)

        res = []

        for x in arr[1:]:
            if not res:
                res.append([x, x])
            else:
                if x == res[-1][1] + 1:
                    res[-1][1] += 1
                else:
                    res.append([x, x])

        return res
        






# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()