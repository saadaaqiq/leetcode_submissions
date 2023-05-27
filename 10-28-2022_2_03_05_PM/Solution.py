# https://leetcode.com/problems/encode-and-decode-strings

class Codec:
    
  def encode(self, strs: List[str]) -> str:
    string = ""
    for j, s in enumerate(strs):
      for c in s:
        if c == "/": string += "//"
        elif c == "+": string += "/+"
        else: string += c
      string += "+" if j < len(strs)-1 else ""
    return string
    

  def decode(self, s: str) -> List[str]:
    l, i = [""], 0
    while i < len(s):
      if s[i]=="/" and i<len(s)-1 and (s[i+1]=="/" or s[i+1]=="+"): l[-1], i = l[-1]+s[i+1], i+1
      elif s[i] == "+": l.append("")
      else: l[-1] += s[i]
      i += 1
    return l