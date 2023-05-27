# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def bit_counter(x):
            s = 0
            while x:
                s += x&1
                x>>=1
            return s
        
        def compare(x, y):
            b1, b2 = bit_counter(x), bit_counter(y)
            if b1 < b2:
                return -1
            elif b1 > b2:
                return 1
            else:
                if x < y:
                    return -1
                elif x > y:
                    return 1
                else:
                    return 0
        
        arr.sort(key=functools.cmp_to_key(compare))
        
        return arr