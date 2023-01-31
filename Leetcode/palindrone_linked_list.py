# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head.next:
            return True
        size = 0
        current = head

        while current:
            size +=1
            current = current.next
        
        leftList = []
        rightList = []

        if size % 2 == 0:
            middleIndex = size/2
            i=0
            current = head
            while current :
                if i < middleIndex:
                    leftList.append(current.val)
                else:
                    rightList.append(current.val)
                current = current.next
                i +=1
            
        else:
            middleIndex = size//2 
            print("middle: ",middleIndex)
            i=0
            current = head
            while current :
                if i==middleIndex:
                    leftList.append(current.val)
                    rightList.append(current.val)
                elif i < middleIndex:
                    leftList.append(current.val)
                else:
                    rightList.append(current.val)
                    
                current = current.next
                i +=1

        
        rightList.reverse()
        print(rightList)
        print(leftList)
        return leftList == rightList



l1 = ListNode()
l1.val = 0
l2 = ListNode()
l2.val = 2
l1.next = l2
l3 = ListNode()
l3.val = 2
l2.next = l3
l4 = ListNode()
l4.val = 1
l3.next = l4

solution = Solution().isPalindrome(l1)

print("solution: ",solution)