# https://leetcode.com/problems/kill-process

class Solution:
  def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    dic = { p : set([p]) for p in pid }
    for i, parent in enumerate(ppid):
      if parent != 0:
        dic[parent].add(pid[i])
    res = set()
    def dfs(process):
      if process in res:
        return
      res.add(process)
      for child in dic[process]:
        dfs(child)
    dfs(kill)
    return res