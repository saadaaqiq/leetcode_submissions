# https://leetcode.com/problems/push-dominoes

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        res = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            if dominoes[i] == "R":
                res[i] = "R"
                while j < n and dominoes[j] == ".":
                    j += 1
                if j == n or dominoes[j] == "R":
                    for k in range(i+1, j):
                        res[k] = "R"
                elif dominoes[j] == "L":
                    p = 1
                    for k in range(i+1, j):
                        res[k] -= p
                        p += 1
            i = j

        i = n-1
        while i >= 0:
            j = i - 1
            if dominoes[i] == "L":
                res[i] = "L"
                while j >= 0 and dominoes[j] == ".":
                    j -= 1
                if j == -1 or dominoes[j] == "L":
                    for k in range(i-1, j, -1):
                        res[k] = "L"
                elif dominoes[j] == "R":
                    p = 1
                    for k in range(i-1, j, -1):
                        res[k] += p
                        p += 1
            i = j

        for i in range(n):
            if isinstance(res[i], int):
                if res[i] == 0:
                    res[i] = "."
                elif res[i] > 0:
                    res[i] = "R"
                elif res[i] < 0:
                    res[i] = "L"

        return "".join(res)
                    