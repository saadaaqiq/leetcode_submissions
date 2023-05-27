# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            while stack and stack[-1][1] >= k:
                char, count = stack.pop()
                if count - k > 0:
                    stack.append([char, count - k])
        
        return ''.join([x[0]*x[1] for x in stack])