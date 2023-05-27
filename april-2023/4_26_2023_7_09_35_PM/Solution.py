# https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if not stack or ((ord(stack[-1])-ord('a'))!=(ord(s[i])-ord('A')) and (ord(stack[-1])-ord('A'))!=(ord(s[i])-ord('a'))):
                stack.append(s[i])
            else:
                stack.pop()
        return ''.join(stack)