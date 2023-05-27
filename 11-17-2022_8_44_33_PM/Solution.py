# https://leetcode.com/problems/bulls-and-cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        c1, c2 = Counter(secret), Counter(guess)
        i = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                c1[secret[i]] -= 1
                c2[guess[i]] -= 1
        for l in c1:
            if c1[l] > 0 and l in c2 and c2[l] > 0:
                b += min(c1[l], c2[l])
        return str(a) + "A" + str(b) + "B"




