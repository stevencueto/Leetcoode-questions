# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #recursive:
        #time complexity is O(n) m O(n):
        
        if not head:
            return None
        
        new_n = head
        if head.next:
            new_n = self.reverseList(head.next)
            head.next.next = head
        head.next = None
            
        return new_n
        
        
        
        
        
        
        
        
        
        
        ##Iterative:
        prv, current = None, head
        
        while crr:
            nxt = current.next
            current.next = prv
            prv = current
            current =  nxt 
        return prev
        #make a variable to move nodes. then return that variable through iteration, 
        #time complexity is O(n) m O (1) only pointers no data strucktures.