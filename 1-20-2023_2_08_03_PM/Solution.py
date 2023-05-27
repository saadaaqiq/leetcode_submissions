# https://leetcode.com/problems/fraction-addition-and-subtraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = []
        w = ""
        for c in expression:
            if w and c == "-" or c == "+":
                fractions.append(w)
                w = ""
            w += c
        fractions.append(w)
        X, Y = [], []
        for frac in fractions:
            X.append(int(frac.split("/")[0]))
            Y.append(int(frac.split("/")[1]))
        p = math.prod(Y)
        for i in range(len(Y)):
            Y[i] = p // Y[i]
        s = sum([X[i]*Y[i] for i in range(len(Y))])
        if s == 0:
            return "0/1"
        if p == 1:
            return str(s) + "/1"
        while math.gcd(int(p),int(s)) != 1:
            d = math.gcd(int(p),int(s))
            p /= d
            s /= d
        return str(int(s)) + "/" + str(int(p))
        


        

        

