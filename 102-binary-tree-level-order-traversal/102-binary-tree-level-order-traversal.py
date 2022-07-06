# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        
        
        
        #iterative:
        
        if not root:
            return []
        
        lvl = 0
        output = []
        q = deque([root,])
        
        while q:
            output.append([])
            length = len(q)
            
            for i in range(length):
                node = q.popleft()
                output[lvl].append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            lvl += 1
            
        return output
        #recursive O(n) O(n)
        
        levels = []
        if not root:
            return levels
        def dfs(node, lvl):
            if len(levels) == lvl:
                levels.append([])
                
            levels[lvl].append(node.val)
            
            if node.left: 
                dfs(node.left, lvl + 1)
            if node.right:
                dfs(node.right, lvl + 1)
        dfs(root, 0)
        return levels