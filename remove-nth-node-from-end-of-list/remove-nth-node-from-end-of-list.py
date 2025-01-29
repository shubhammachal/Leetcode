# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #create dummy to handle edge cases
        dummy = ListNode() #default value is 0
        dummy.next = head
        ahead = behind = dummy
        #move ahead to n + 1
        for _ in range(n+1):
            ahead = ahead.next
        #move both pointers keeping the distance n + 1 between them
        while ahead:
            ahead = ahead.next
            behind = behind.next
        #as ahead points to None, behind will be the node previous to node to be removed
        #update behind.next
        behind.next = behind.next.next
        return dummy.next
       