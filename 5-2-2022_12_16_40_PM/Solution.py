# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        po, pc, bo, bc, co, cc = "(", ")", "[", "]", "{", "}"
        for c in s:
            if c == po or c == bo or c == co:
                stack.append(c)
            elif not stack or (c == pc and stack.pop() != po) or (c == bc and stack.pop() != bo) or (c == cc and stack.pop() != co):
                return False
        return True if not stack else False