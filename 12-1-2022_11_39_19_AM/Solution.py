# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        return round(3*(((1/3)*((19 + 3*sqrt(33))**(1/3) + (19-3*sqrt(33))**(1/3) + 1))**n * ((586+102*sqrt(33))**(1/3)))/((586+102*sqrt(33))**(2/3) + 4 - 2*(586+102*sqrt(33))**(1/3)))