# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        l = len(digits)
        keyboard = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        d = [keyboard[int(c)] for c in digits]
        p = [0] * l 
        while True:
            if p[0] == len(d[0]):
                return res
            res.append(''.join( [ d[i][p[i]] for i in range(len(p)) ] ))
            j = len(p) - 1
            p[j] += 1
            while j > 0 and p[j] == len(d[j]):
                p[j] = 0
                p[j-1] += 1
                j-=1
        

            


