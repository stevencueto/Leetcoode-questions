# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ##
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) 
        return False
    
    
        #iterative:
        if not q and not p:
            return True
        
        pQ = deque([p])
        qQ = deque([q])
        
        while len(q):
            nodeQ = q.pop()
            nodeQ
            
        
        
        # DFS: T O(q + p) S O(1)
        if not q and not p:
            return True
        if not q or not p or q.val != p.val:
            return False
        
        return (self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left))