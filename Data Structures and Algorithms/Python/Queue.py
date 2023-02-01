class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self,index):
        return self.queue[index]
    def get(self):
        return self.queue


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("before: ",q.get())

print("peek b4: ",q.peek(1))

print("dequeue: ",q.dequeue())
print("after: ",q.get())
print("peek after: ",q.peek(1))