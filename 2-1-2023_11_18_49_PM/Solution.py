# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, arr: List[str]) -> bool:
        vis = set()
        q = deque([0])
        while q:
            k = q.pop()
            if k == len(s):
                return True
            for w in arr:
                if len(w) + k <= len(s) and w == s[k:k+len(w)] and k + len(w) not in vis:
                    vis.add(k + len(w))
                    q.append(k + len(w))
        return False