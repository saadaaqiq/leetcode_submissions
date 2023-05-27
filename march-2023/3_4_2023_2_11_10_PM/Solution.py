# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        stack = [0]
        queue = collections.deque()

        for i in range(m):
            while stack:
                if t[stack[-1]] != s[i]:
                    stack.pop()
                else:
                    queue.append(stack.pop())
            while queue:
                y = queue.popleft() + 1
                if y == n:
                    return i - n + 1
                stack.append(y)
            stack.append(0)
        
        return -1
            