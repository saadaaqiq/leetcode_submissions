# https://leetcode.com/problems/meeting-scheduler

class Solution:
  def minAvailableDuration(self, bob, alice, duration):
    i, j = 0, 0
    bob.sort(key= lambda x:x[0])
    alice.sort(key= lambda x:x[0])
    while i < len(bob) and j < len(alice):
      bob_start, bob_end, alice_start, alice_end = bob[i][0], bob[i][1], alice[j][0], alice[j][1]
      if bob_start >= alice_end:
        j += 1
      elif alice_start >= bob_end:
        i += 1
      elif bob_start <= alice_start and bob_end > alice_start and bob_end < alice_end:
        if bob_end - alice_start >= duration:
          return [alice_start, alice_start + duration]
        i += 1
      elif alice_start <= bob_start and alice_end > bob_start and alice_end < bob_end:
        if alice_end - bob_start >= duration:
          return [bob_start, bob_start + duration]
        j += 1
      elif bob_start >= alice_start and bob_end <= alice_end:
        if bob_end - bob_start >= duration:
          return [bob_start, bob_start + duration]
        i += 1
      elif alice_start >= bob_start and alice_end <= bob_end:
        if alice_end - alice_start >= duration:
          return [alice_start, alice_start + duration]
        j += 1
      else:
        return []
    
    return []