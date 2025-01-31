class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #base case
        if not root:
            return None
        #first case if p or q is root, LCA is root
        if p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #One of p or q is in the left subtree, and the other one is in the right subtree. The root must be the answer because it is the connection point between the two subtrees, and thus the lowest node to have both p and q as descendants.

        if left and right:
            return root
        #Both p and q are in one of the subtrees. In that case, the root is not the answer because we could look inside the subtree and find a "lower" node.

        if left:
            return left
        if right:
            return right
        
