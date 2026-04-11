# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(nod1,nod2):
            if not nod1 and not nod2:
                return True

            if nod1 and not nod2:
                return False

            if nod2 and not nod1:
                return False

            if nod1.val != nod2.val:
                return False

            left = helper(nod1.left,nod2.left)
            right = helper(nod1.right,nod2.right)

            return left and right
        return helper(p,q)
        
        

        