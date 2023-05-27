# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for w, l in matches:
            if w not in dic: dic[w] = 0
            if l not in dic: dic[l] = 0
            dic[l] += 1
        answer = [[], []]
        for k in dic:
            if dic[k] == 0:
                answer[0].append(k)
            elif dic[k] == 1:
                answer[1].append(k)
        answer[0].sort()
        answer[1].sort()
        return answer

            