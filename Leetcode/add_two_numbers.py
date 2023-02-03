from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        str = f" {self.val} "
        current = self.next

        while current:
            str += f" {current.val} "
            current = current.next
        return str
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNumber = ""
        secondNumber = ""
        current= l1
    
        while current:
            firstNumber += str(current.val)
            current = current.next
        
        current = l2

        while current:
            secondNumber += str(current.val)
            current = current.next
        
        firstNumber = int(firstNumber[::-1])
        secondNumber = int(secondNumber[::-1])

        print("firstNumber: ",firstNumber)
        print("secondNumber: ",secondNumber)

        sum = str(firstNumber + secondNumber)

        print("sum: ",sum)

        l3 = ListNode(sum[0])

        for i in range(1,len(sum)):
            
            old = l3
            new = ListNode(sum[i])
            l3 = new
            l3.next = old

        return l3

l1 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)

l11.next  = l12
l1.next = l11

l2 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)


l21.next = l22
l2.next = l21

results = Solution().addTwoNumbers(l1,l2)

print(results)



            


        

            