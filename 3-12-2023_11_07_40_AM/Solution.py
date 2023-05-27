# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

class Solution:
    def sortedListToBST(self, head):

        def func(node):
            if not node:
                return None
            elif not node.next:
                return TreeNode(node.val)
            elif not node.next.next:
                N = TreeNode(node.val)
                N.right = TreeNode(node.next.val)
                return N
            elif not node.next.next.next:
                N = TreeNode(node.next.val)
                N.left = TreeNode(node.val)
                N.right = TreeNode(node.next.next.val)
                return N
            else:
                premid, mid, fast = None, node, node
                while fast and fast.next:
                    premid = mid
                    mid = mid.next
                    fast = fast.next.next
                
                premid.next = None
                L = func(node)

                r_node = mid.next
                mid.next = None
                R = func(r_node)

                N = TreeNode(mid.val)
                N.left = L
                N.right = R
                return N

        print([i for i in range(100)])

        return func(head)
