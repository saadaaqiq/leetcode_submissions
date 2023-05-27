# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * len(labels)
        adj = collections.defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        ans = [1] * len(labels)

        vis = set()

        def dfs(i):
            arr = [0] * 26
            arr[ord(labels[i]) - 97] += 1
            vis.add(i)
            if not adj[i]:
                return arr
            for j in adj[i]:
                if j not in vis:
                    tab = dfs(j)
                    for k in range(26):
                        arr[k] += tab[k]
            ans[i] = arr[ord(labels[i]) - 97]
            return arr
            
        dfs(0)

        return ans