# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def height(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            max_diameter = max(max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        height(root)
        return max_diameter