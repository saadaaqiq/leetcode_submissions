# https://leetcode.com/problems/design-a-leaderboard

class Leaderboard:

  def __init__(self):
    self.scores = {}

  def addScore(self, playerId: int, score: int) -> None:
    if playerId not in self.scores:
      self.scores[playerId] = 0
    self.scores[playerId] += score

  def top(self, k: int) -> int:
    return sum(sorted(self.scores.values(), reverse=True)[:k])

  def reset(self, playerId: int) -> None:
    self.scores.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)