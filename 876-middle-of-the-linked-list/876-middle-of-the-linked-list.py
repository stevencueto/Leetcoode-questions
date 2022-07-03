# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        #less efficient solution, with extra memory:
        
        queue = [head]
        
        while queue[-1].next:
            queue.append(queue[-1].next)
        return queue[len(queue) // 2]
        
        
        #Pointer solution, more efficient, no extra memory
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    #by the time the fast one gets to the end of the linked list, we are in the middle, so we return the middle.
    #O(n) O(1)