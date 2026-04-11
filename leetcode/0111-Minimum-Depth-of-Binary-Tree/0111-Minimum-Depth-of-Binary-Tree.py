# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return float('inf')
                
            left = helper(node.left)
            right = helper(node.right)
            
            ans = min(left,right)

            return (1 + ans) if ans != float('inf') else 1

        if not root:
            return 0

        return helper(root)