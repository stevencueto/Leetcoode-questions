# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res
        q = collections.deque([root])
        
        while q:
            right_n = None
            qlen = len(q)
            
            for i in range(qlen):
                node = q.popleft()
                if node:
                    right_n = node
                    q.append(node.left)
                    q.append(node.right)
            if right_n:
                res.append(right_n.val)
        return res