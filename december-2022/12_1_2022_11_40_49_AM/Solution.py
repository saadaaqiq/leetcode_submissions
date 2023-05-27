# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        r33 = sqrt(33)
        return round(3*(((1/3)*((19 + 3*r33)**(1/3) + (19-3*r33)**(1/3) + 1))**n * ((586+102*r33)**(1/3)))/((586+102*r33)**(2/3) + 4 - 2*(586+102*r33)**(1/3)))