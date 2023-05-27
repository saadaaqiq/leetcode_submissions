# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        i, j = 0, len(skill)-1
        teams = []
        while i < j:
          teams.append([skill[i], skill[j]])
          i += 1
          j -= 1
        const = teams[0][0] + teams[0][1]
        res = teams[0][0] * teams[0][1]
        for i in range(1, len(teams)):
          if teams[i][0] + teams[i][1] != const:
            return -1
          else:
            res += teams[i][0] * teams[i][1]
        return res
        
        