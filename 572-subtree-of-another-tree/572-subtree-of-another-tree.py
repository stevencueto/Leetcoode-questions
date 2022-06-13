# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, tree: TreeNode, subTree: TreeNode) -> bool:
        if not subTree:
            return True
        if not tree:
            return False
        if self.sameTree(tree, subTree):
            return True
        return (self.isSubtree(tree.left, subTree) or self.isSubtree(tree.right, subTree))
    
    def sameTree(self, t, s):
        if not t and not s:
            return True
        if t and s and t.val == s.val:
            return (self.sameTree(t.left, s.left) and self.sameTree(t.right, s.right)) 
        return False