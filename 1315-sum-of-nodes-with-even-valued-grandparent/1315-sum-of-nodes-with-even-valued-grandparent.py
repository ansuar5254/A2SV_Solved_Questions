# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def helper(node,parent,grandparent):
            if not node:
                return 0

            total = 0

            if grandparent and grandparent.val % 2 == 0:
                total += node.val


            total += helper(node.left,node,parent)
            total += helper(node.right,node,parent)
            return total

        return helper(root,None,None)

        