# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def nodemaker(i,j):
      if i > j:
        return None
      if i == j:
        return TreeNode(nums[i])
      mid = (i+j)//2
      return TreeNode(nums[mid], nodemaker(i,mid-1), nodemaker(mid+1,j))
    return nodemaker(0,len(nums)-1)