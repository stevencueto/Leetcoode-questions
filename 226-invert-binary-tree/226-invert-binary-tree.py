# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #iterative:
        #time complexity is O(n), space complexity is O(n) need to make a queue
#         q = collections.deque([root])
        
#         while len(q):
#             node = q.popleft()
            
#             if node != None:
#                 tmp = node.left
#                 node.left = node.right
#                 node.right = tmp
                
#                 q.append(node.left)
#                 q.append(node.right)
#         return root
        
        
        #recursion:
        #time complexity is O(n) space complexity is O(1) no new data structures
        
        if not root:
            return None
        tmr = root.right
        root.right = root.left
        root.left = tmr
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root