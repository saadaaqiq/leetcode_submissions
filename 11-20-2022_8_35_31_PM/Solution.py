# https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:
        stack = ["("]
        s += ")"

        for i in range(len(s)):
            if s[i] == " ":
                continue
            elif s[i] in ["+", "-", "("]:
                stack.append(s[i])
            elif s[i].isnumeric():
                if not stack or not stack[-1].isnumeric(): 
                    stack.append(s[i])
                else:
                    stack[-1] += s[i]
            elif s[i] == ")":
                sm = 0
                while stack and stack[-1] != "(":
                    c = int(stack.pop())
                    while stack[-1] in ["+", "-"]:
                        sign = stack.pop()
                        if sign == "-":
                            c = -c
                    sm += c
                if stack:
                    stack.pop()
                    stack.append(str(sm))
        return stack[0]