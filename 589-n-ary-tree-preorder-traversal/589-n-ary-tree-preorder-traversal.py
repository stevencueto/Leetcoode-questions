"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ##dfs O(n) O(n)
        output = []
        def dfs(node):
            if not node:
                return None
            
            output.append(node.val)
            
            for c in node.children:
                dfs(c)
        dfs(root)
        
        return output