# https://leetcode.com/problems/erect-the-fence

class Solution:
    # Graham Scan
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        xx, yy = min(trees, key=lambda tree: (tree[1], tree[0]))  
        mp = {}
        for x, y in trees: 
            mp.setdefault(atan2(y-yy, x-xx), []).append([x, y])
        
        trees = []
        m = max(mp)
        for k in sorted(mp): 
            mp[k].sort(key=lambda p: abs(p[0]-xx)+abs(p[1]-yy))
            if k == m and trees: mp[k].reverse()
            trees.extend(mp[k])
                
        stack = []
        for x, y in trees: 
            while len(stack) >= 2: 
                x0, y0 = stack[-1]
                x1, y1 = stack[-2]
                if (x0-x1)*(y-y0) - (x-x0)*(y0-y1) >= 0: break
                else: stack.pop()
            stack.append([x, y])
        return stack
        
