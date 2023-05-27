# https://leetcode.com/problems/count-items-matching-a-rule

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        ind = 0 if ruleKey == "type" else (1 if ruleKey == "color" else 2)
        res = 0
        for X in items:
            if X[ind] == ruleValue:
                res += 1
        return res