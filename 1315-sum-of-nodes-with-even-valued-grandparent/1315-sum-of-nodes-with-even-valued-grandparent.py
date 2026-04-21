# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0
        def helper(node,parent,g_parant):
            nonlocal total
            if not node:
                return 0

            if g_parant and g_parant.val % 2 ==0:
                total += node.val


            helper(node.left,node,parent)
            helper(node.right,node,parent)

        helper(root,None,None)
        return total


        