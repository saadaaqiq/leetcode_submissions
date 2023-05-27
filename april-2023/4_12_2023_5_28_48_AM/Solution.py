# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for w in arr:
            if not w or w == "." or (not stack and w == ".."):
                continue
            if w == "..":
                stack.pop()
            else:
                stack.append(w)
        return "/" + "/".join(stack)