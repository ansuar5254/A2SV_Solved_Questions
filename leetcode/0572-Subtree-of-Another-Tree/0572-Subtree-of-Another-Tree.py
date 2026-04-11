# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(nod1,nod2):
            if not nod1 and not nod2:
                return True
            if not nod1 or not nod2:
                return False

            if nod1.val != nod2.val:
                return False

            return helper(nod1.left,nod2.left) and helper(nod1.right,nod2.right)

        if not root:
            return False

        if helper(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)