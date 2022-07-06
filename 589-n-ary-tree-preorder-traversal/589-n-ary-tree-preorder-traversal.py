"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
            
        return output
        
        
        
        
        
        ##dfs O(n) O(n) or recursive
        output = []
        def dfs(node):
            if not node:
                return None
            
            output.append(node.val)
            
            for c in node.children:
                dfs(c)
        dfs(root)
        
        return output