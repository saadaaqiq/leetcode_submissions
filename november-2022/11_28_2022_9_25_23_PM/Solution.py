# https://leetcode.com/problems/basic-calculator-ii

class Solution:
  def calculate(self, s: str) -> int:
    arr = []
    ops = ["+", "-", "/", "*"]

    for c in s:
      if c == " ": continue
      if not arr or c in ops or arr[-1] in ops: arr.append(c)
      else: arr[-1] += c
    for i, elem in enumerate(arr):
      if elem.isnumeric():
        arr[i] = int(arr[i])

    for i in range(len(arr)):
      if arr[i] == "*" or arr[i]=="/":
        l,r = i-1,i+1
        while l>=0 and arr[l]=="": l-=1
        while r<len(arr) and arr[r]=="": r+=1 
        arr[i] = arr[l]*arr[r] if arr[i]=="*" else int(arr[l]/arr[r])
        arr[l] = ""
        arr[r] = ""
    for i in range(len(arr)):
      if arr[i] == "-" or arr[i]=="+":
        l,r = i-1,i+1
        while l>=0 and arr[l]=="": l-=1
        while r<len(arr) and arr[r]=="": r+=1 
        arr[i] = arr[l]-arr[r] if arr[i]=="-" else arr[l]+arr[r]
        arr[l] = ""
        arr[r] = ""
    for i in range(len(arr)):
      if arr[i]!="":
        return arr[i]