# https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        j = 0
        for i in range(n):
            stack.append(pushed[i])
            while j < n and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0