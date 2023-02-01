class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None
    
    def __repr__(self):
        return f"<Node: {self.val}>"


class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def size(self): 
        size = 0
        current = self.head
        while current:
            size +=1
            current = current.next

        return size

    def addHead(self,val):
        new = Node(val)

        if not self.head:
            self.head = new
            return
        else:
            new.next = self.head
            self.head = new
    
    def addTail(self,val):
        new = Node(val)

        if not self.head:
            self.head = new
            return 
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new
        
    def addAtPosition(self, position,val):
        if position < 1 or position > self.size():
            print(f"invalid position: {position}")
            return
        elif position == 1:
            self.addHead(val)
            return
        elif position == 2 and not self.head.next:
            new = Node(val)
            self.head.next = new

        new = Node(val)
        current = self.head.next
        previous = self.head
        while position > 2:
            previous = current
            current = current.next
            position -= 1
        
        previous.next = new
        new.next = current


    
    def __repr__(self):
        output = f"<Head: {self.head.val}>"

        if not self.head.next:
            return output

        current =self.head.next
        while current.next:
            output += f" -> {current.val}"
            current = current.next
        
        output += f" -> <Tail: {current.val}>"

        return output


head = Node(1)

ll = LinkedList(head)

ll.addHead(2)
ll.addHead(3)
ll.addHead(4)
ll.addHead(5)
ll.addHead(6)
ll.addHead(7)
ll.addHead(8)
ll.addHead(9)
ll.addHead(10)
# ll.addTail(0)
ll.addAtPosition(4,4)
ll.addAtPosition(2,4)
ll.addAtPosition(100,20)


print("size: ",ll.size())

print(ll)
    
