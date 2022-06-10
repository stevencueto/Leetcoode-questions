# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        make a while loop to lopp through the linked list, if  are not empty, the continue, we are going to check whether l1 is < than l2, 
        when we exit our while loop, we have will check if one of them is null, then make the next node, as the node that is left.
        """
        dummy = ListNode()
        #make a new ListNode
        tail = dummy
        #make a reference to the node
        
        while l1 and l2:
            #while we have the 2 nodes, compare values. if the l1 is less then make it the .next value, esle the l2
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            #make sure to extend the tail even more for the reference    
            tail = tail.next
            
            
            
            #if we still have nodes on either one of the list, append it to the tail
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
           
        #return the dummy reference node.
        return dummy.next
            
        