# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.c = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        #travers through the tree, recursively and find start with infinity values to veirfy weather or not the tree is valid, repeat this for every node in the tree.
        
        def valid (node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float('-inf'), float("inf"))