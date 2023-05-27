# https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        m, ind, l = 20001, 0, len(arr)
        for i, n in enumerate(arr):
            (m, ind) = (abs(x-n), i) if abs(x-n)<m else (m, ind)
        res = [arr[ind]]
        i, j, c = ind-1, ind+1, 1
        while c < k and (i>=0 or j<l):
            if i >= 0 and j < l:
                if abs(arr[i]-x)<=abs(arr[j]-x):
                    res.append(arr[i])
                    i-=1
                else:
                    res.append(arr[j])
                    j+=1
            elif i==-1:
                res.append(arr[j])
                j+=1
            elif j==l:
                res.append(arr[i])
                i-=1
            c+=1
        return sorted(res)
