# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root):
        def sumTree(node):
            if not node:
                return 0
            return sumTree(node.left) + sumTree(node.right) + node.val
        
        total_sum = sumTree(root)
        if total_sum % 2 == 1:
            return False
        
        target_sum = total_sum // 2
        found = False  # ✅ Flag to track if we found a partition
        
        def dfs(node):
            nonlocal found
            if not node or found:  # Early termination
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            current_sum = left_sum + right_sum + node.val
            
            if node != root and current_sum == target_sum:
                found = True
            
            return current_sum
        
        dfs(root)  # ✅ Actually call the function!
        return found