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
        q = deque([root])
        
        while len(q) > 0:
            node = q.popleft()
            
            if node != None:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                
                q.append(node.left)
                q.append(node.right)
        return root
        
        
        #recursion:
        #time complexity is O(n) space complexity is O(1) no new data structures
        if not root:
            return None
        
        if not root:
            return None
        
        #swap the children in the bnt
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root