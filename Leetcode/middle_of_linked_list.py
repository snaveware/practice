from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        size = 0
        
        current = head
        while current :
            size +=1
            current = current.next
        
        middleIndex = size//2

        current = head
        i = 0

        while i != middleIndex :
            current = current.next
            i += 1
        
        return current


        
