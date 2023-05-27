# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if stack and ((c==')' and stack[-1]=='(') or (c==']' and stack[-1]=='[') or (c=='}' and stack[-1]=='{')):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0