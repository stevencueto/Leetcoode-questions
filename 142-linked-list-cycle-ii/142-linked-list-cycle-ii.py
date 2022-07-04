# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #optima solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        catch = self.catch(head)
        
        if catch is None:
            return None
        
        #make pointers to traverse, then if they meet stop loop, and return meeting point!
        
        p1 = head
        p2 = catch
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
    
    
    
    
    def catch (self, head):
        if head is None:
            return None
        
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return slow
            
        return None
    #extra memory approach
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        
        node = head
        
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        
        return None
    
    #make a set, add the nodes to the set if we find an existing node in the set, then we return the node, else we add it to the set and them update the node,, O(n) O(n) not so efficient approach
    
    
    