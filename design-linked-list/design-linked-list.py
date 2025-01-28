class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next #head is dummy node
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+= 1
            curr = curr.next
        return -1 #if index not found
            

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        if not new_node.next:
            self.tail = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next
            if predecessor is None:
                return  # Index out of bounds
        new_node = ListNode(val)
        new_node.next = predecessor.next
        predecessor.next = new_node
        # Update tail if new node is the last node
        if new_node.next is None:
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next
            if predecessor is None:
                return  # Index out of bounds
        if predecessor.next is None:
            return  # No node to delete
        # Update tail if deleting the current tail
        if predecessor.next == self.tail:
            self.tail = predecessor
        # Delete the node
        predecessor.next = predecessor.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)