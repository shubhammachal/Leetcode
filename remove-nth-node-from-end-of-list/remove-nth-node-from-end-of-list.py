# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #find length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
            
        #if node to be removed is head
        if length == n:
            return head.next
        
        #find previous of the node to be removed
        prev = head
        for _ in range(length - n - 1):
            prev = prev.next
        #update previous to the next of node to be removed
        prev.next = prev.next.next
        return head