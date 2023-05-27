# https://leetcode.com/problems/encode-and-decode-strings

class Codec:
    
  def encode(self, strs: List[str]) -> str:
    string = ""
    for j, s in enumerate(strs):
      for i,c in enumerate(s):
        if c == "/": string += "//"
        elif c == "+": string += "/+"
        else: string += c
      string += "+" if j < len(strs)-1 else ""
    return string
    

  def decode(self, s: str) -> List[str]:
    l = [""]
    i = 0
    while i < len(s):
      if s[i] == "/" and i < len(s)-1 and s[i+1] == "/":
        l[-1] += "/"
        i += 2
      elif s[i] == "/" and i < len(s)-1 and s[i+1] == "+":
        l[-1] += "+"
        i += 2
      elif s[i] == "+":
        l.append("")
        i += 1
      else:
        l[-1] += s[i]
        i += 1
    return l