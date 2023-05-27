# https://leetcode.com/problems/design-tic-tac-toe

class TicTacToe:

  def __init__(self, n: int):
    self.n = n
    self.p1_rows = [0] * n
    self.p1_cols = [0] * n
    self.p1_o1 = 0
    self.p1_o2 = 0
    self.p2_rows = [0] * n
    self.p2_cols = [0] * n
    self.p2_o1 = 0
    self.p2_o2 = 0
    
  def move(self, row: int, col: int, player: int) -> int:
    if player == 1:
      self.p1_rows[row] += 1
      if self.p1_rows[row] == self.n: return 1
      self.p1_cols[col] += 1
      if self.p1_cols[col] == self.n: return 1
      self.p1_o1 = self.p1_o1+1 if row == col else self.p1_o1
      if self.p1_o1 == self.n: return 1
      self.p1_o2 = self.p1_o2+1 if row + col == self.n-1 else self.p1_o2
      if self.p1_o2 == self.n: return 1
    else:
      self.p2_rows[row] += 1
      if self.p2_rows[row] == self.n: return 2
      self.p2_cols[col] += 1
      if self.p2_cols[col] == self.n: return 2
      self.p2_o1 = self.p2_o1+1 if row == col else self.p2_o1      
      if self.p2_o1 == self.n: return 2
      self.p2_o2 = self.p2_o2+1 if row + col == self.n-1 else self.p2_o2
      if self.p2_o2 == self.n: return 2
    return 0