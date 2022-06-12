# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, crr = None, head
        
        while crr:
            nxt = crr.next
            crr.next = prev
            prev = crr
            crr =  nxt 
        return prev
        #make a variable to move nodes. then return that variable through iteration, 