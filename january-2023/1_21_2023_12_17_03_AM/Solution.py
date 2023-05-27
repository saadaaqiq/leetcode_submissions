# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        k = len(digits)
        res = []
        keyboard = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        d = [keyboard[int(c)] for c in digits]
        
        curr = []
        def comb(i):
            if i == k:
                res.append(''.join(curr))
                return
            for c in d[i]:
                curr.append(c)
                comb(i+1)
                curr.pop()
            return

        comb(0)
        return res

            


