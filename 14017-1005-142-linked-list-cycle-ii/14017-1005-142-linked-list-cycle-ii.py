# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #check for cycle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #if cycle exits the loop
            if slow == fast:
                break
        #if we exit without break, no cycle exists
        else:
            return None

        #reset fast to head and move fast and slow with same speed
        #they will meet at the node where cycle starts
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow