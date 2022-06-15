# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        an = root
        
        while an:
            if p.val > an.val and q.val > an.val:
                an = an.right
            elif p.val < an.val and q.val < an.val:
                an = an.left
            else:
                return an
            
            
    #we are guaranteed to find a result, so in this case we dont not an empty result, we are going to check in a while loop, if the ancestor  "an" is greater than p and q then we move to the right, else if is lower than p and q, we move to the right, else we found our an so we just return that, time O(log n) one node for every single level in the tree, so the time complexity is the hight of the tree.