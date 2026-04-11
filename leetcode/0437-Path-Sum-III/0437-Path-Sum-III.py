# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def helper(node,curr_sum):

            if not node:
                return 
            curr_sum += node.val
            if curr_sum == targetSum:
                self.count += 1
            helper(node.left,curr_sum)
            helper(node.right,curr_sum)

        def dfs(nod):

            if not nod:
                return 

            helper(nod,0)
            dfs(nod.left)
            dfs(nod.right)
            
        dfs(root)
        return self.count