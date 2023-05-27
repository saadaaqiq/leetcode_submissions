# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, arr, target):
        res = set()
        curr = []
        s = 0

        arr.sort(reverse=True)

        def comb(i):
            nonlocal s
            if s > target:
                return
            elif s == target:
                res.add(tuple(curr))
            else:
                if i == len(arr):
                    return
                # include i 
                curr.append(arr[i])
                s += arr[i]
                # and stay on i 
                comb(i)
                # and go to i+1
                comb(i+1)
                curr.pop()
                s -= arr[i]

                # don't include i
                comb(i+1)
                return 

        comb(0)

        return res


