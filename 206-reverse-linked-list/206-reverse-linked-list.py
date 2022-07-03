# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #make pointer:
        prev, curr = None, head
        
        
        #iterate:
        while curr:
            #store curr in a variable:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
        #make a variable to move nodes. then return that variable through iteration, 
        #time complexity is O(n) m O (1) only pointers no data strucktures.
        
        
          #recursive:
        #time complexity is O(n) m O(n):
        # the memory is linerar because if we were given a list of size 2 the recursive call is size 2 as well
        
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head
        
        