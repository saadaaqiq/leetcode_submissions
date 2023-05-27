# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        its = []
        for inter in intervals:
            its = self.insert(its,inter)
        return its
    
    def insert(self, its: List[List[int]], nit: List[int]) -> List[List[int]]:
        x = nit[0]
        y = nit[1]
        
        i=0
        j=len(its) - 1
        sup = (j-i)//2
        
        if not its or (x<its[i][0] and y>its[j][1]):
            return [nit]
        
        while j>i:
            if y < its[sup][0]:
                j = sup - 1
            else:
                if y <= its[sup][1]:
                    break
                else:
                    i = sup + 1
            sup = i + (j-i)//2
        
        i=0
        j=len(its) - 1
        inf = (j-i)//2
        
        while j>i:
            if x > its[inf][1]:
                i = inf + 1
            else:
                if x >= its[inf][0]:
                    break
                else:
                    j = inf - 1
            inf = i + (j-i)//2
        
        before = []
        after = []
        middle = []
        xprime = x
        yprime = y
        if y < its[0][0]:
            before = [nit]
            after = its
        elif x > its[len(its)-1][1]:
            before = its
            after = [nit]
        else:
            xprime = x if x>its[inf][1] else min(x, its[inf][0])
            yprime = y if y<its[sup][0] else max(y,its[sup][1])
            if inf==-1:
                before = its[:inf+1] if x>its[inf+1][1] else its[:inf+1]
            else:
                before = its[:inf+1] if x>its[inf][1] else its[:inf]
            if len(its) == 2 and inf == -1:
                before = []
            after = its[sup:] if y<its[sup][0] else its[sup+1:]
            middle = [[xprime, yprime]]
                
        return before + middle + after
        