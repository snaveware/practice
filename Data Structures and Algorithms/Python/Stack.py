class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def get(self):
        return self.stack
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("before: ",s.get())
val = s.pop()
print(val)

print("after: ",s.get())

print("is Empty: ",s.isEmpty())