# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, arr, target):
        res = set()
        curr = []
        s = 0

        arr.sort()
        while arr and arr[-1] > target:
            arr.pop()
        arr.reverse()

        def comb(i):
            nonlocal s
            if s > target:
                return
            elif s == target:
                res.add(tuple(curr))
            else:
                if i == len(arr):
                    return
                # include i and stay on i 
                curr.append(arr[i])
                s += arr[i]
                comb(i)
                curr.pop()
                s -= arr[i]

                # include i and go to i+1
                curr.append(arr[i])
                s += arr[i]
                comb(i+1)
                curr.pop()
                s -= arr[i]

                # don't include i
                comb(i+1)
                return 

        comb(0)

        return res


