# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbalanced = True
        
        def height(node):
            nonlocal isbalanced
            if not node:
                return 0

            if not isbalanced:
                return 0
            left_height = height(node.left)

            if not isbalanced:
                return 0

            right_height = height(node.right)

            if not isbalanced:
                return 0

            if abs(left_height - right_height) > 1:
                isbalanced = False
            return max(left_height, right_height) + 1
            
        height(root)
        return isbalanced