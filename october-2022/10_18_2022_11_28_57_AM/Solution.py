# https://leetcode.com/problems/missing-number-in-arithmetic-progression

class Solution:
  def missingNumber(self, arr: List[int]) -> int:
    if arr[1]-arr[0] > 0:
      for i in range(1, len(arr)-1):
        if arr[i+1]-arr[i] > arr[1]-arr[0]:
          return arr[i] + arr[1]-arr[0]
        elif arr[i+1]-arr[i] < arr[1]-arr[0]:
          return arr[0] + arr[i+1]-arr[i] 
    elif arr[len(arr)-2]-arr[len(arr)-1] > 0:
      for i in range(len(arr)-2, -1, -1):
        if arr[i-1]-arr[i] > arr[len(arr)-2]-arr[len(arr)-1]:
          return arr[i] + arr[len(arr)-2]-arr[len(arr)-1]
        elif arr[i-1]-arr[i] < arr[len(arr)-2]-arr[len(arr)-1]:
          return arr[len(arr)-1] + arr[i-1]-arr[i]
    else:
      return arr[0]