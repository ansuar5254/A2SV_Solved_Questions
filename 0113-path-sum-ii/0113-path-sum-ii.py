# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helper(node,curr_sum,temp):
            if not node:
                return 
            temp.append(node.val)
            curr_sum += node.val
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    ans.append(temp[::])
                    
            helper(node.left,curr_sum,temp)
            helper(node.right,curr_sum,temp)
            temp.pop()
        helper(root,0,[])
        return ans

            
                
        