# https://leetcode.com/problems/different-ways-to-add-parentheses

class Solution:
    def diffWaysToCompute(self, string: str) -> List[int]:
        if string.isnumeric():
            return [int(string)]
        ans = []
        for i, c in enumerate(string):
            if c in "+*-":
                left, right = self.diffWaysToCompute(string[:i]), self.diffWaysToCompute(string[i+1:])
                for l in left:
                    for r in right:
                        if c=="+":
                            ans.append(l+r)
                        elif c=="-":
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        return ans
        
