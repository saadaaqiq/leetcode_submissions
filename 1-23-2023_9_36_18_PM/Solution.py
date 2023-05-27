# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        b = [0] * 17
        arr = [0]
        for i in range(n):
            if b[16] == 0:
                b[16] = 1
                arr.append(arr[-1] + 1)
            else:
                x = 0
                j = 16
                while b[j] == 1:
                    x += 1
                    b[j] = 0
                    j -= 1
                b[j] = 1
                arr.append(arr[-1] - x + 1)
        return arr
