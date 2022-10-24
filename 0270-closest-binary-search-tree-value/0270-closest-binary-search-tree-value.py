# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        candidate = root.val
        
        while node:
            candidate = min((candidate, node.val), key =lambda x: abs(x - target))
            if node.val < target:
                node = node.right
            elif node.val > target:
                node = node.left
            else:
                return node.val
        return candidate