class MinHeap :
    def __init__(self):
        self.size = 0
        self.minHeap = list()

    def getParentIndex(self,childIndex): 
        return (childIndex-1)//2
    
    def getLeftChildIndex(self,parentIndex):
        return 2*parentIndex+1

    def getRigtChildIndex(self,parentIndex):
        return 2*parentIndex+2

    def hasParent(self,childIndex):
        return self.getParentIndex(childIndex) >= 0

    def hasLeftchild(self,parentIndex): 
        return self.getLeftChildIndex(parentIndex) < self.size

    def hasRightChild(self,parentIndex):
        return self.getRigtChildIndex(parentIndex) < self.size

    def getParent(self,childIndex):
        return self.minHeap[self.getParentIndex(childIndex)]

    def getLeftchild(self,parentIndex):
        return self.minHeap[self.getLeftChildIndex(parentIndex)]

    def getRightChild(self,parentIndex):
        return self.minHeap[self.getRigtChildIndex(parentIndex)]

    def swap(self,index1,index2):
        temp = self.minHeap[index1]
        self.minHeap[index1] = self.minHeap[index2]
        self.minHeap[index2] = temp

    def insert(self,value):
        self.minHeap.append(value)
        self.size += 1
        # self.iterativeUpHeap()
        self.recursiveUpHeap(self.size-1)
    
    def removeMin(self):
        min = self.minHeap[0]

        self.minHeap[0] = self.minHeap.pop()
        self.size -= 1
        # self.iterativeDownHeap()
        self.recursiveDownHeap(0)

        return min

    def iterativeUpHeap(self):
        currentIndex = self.size-1
        while self.hasParent(currentIndex) and self.getParent(currentIndex) > self.minHeap[currentIndex]:
            self.swap(currentIndex,self.getParentIndex(currentIndex))
            currentIndex = self.getParentIndex(currentIndex)

    def iterativeDownHeap(self):
        currentIndex = 0

        while self.hasLeftchild(currentIndex):
            minValueIndex =self.getLeftChildIndex(currentIndex)
            
            if self.hasRightChild(currentIndex) and self.getRightChild(currentIndex) < self.minHeap[minValueIndex]:
                minValueIndex = self.getRigtChildIndex(currentIndex)

            if self.minHeap[minValueIndex] > self.minHeap[currentIndex]:
                break
            else: 
                self.swap(minValueIndex,currentIndex)
            
            currentIndex = minValueIndex
    
    def recursiveUpHeap(self,currentIndex):
        if self.hasParent(currentIndex) and self.getParent(currentIndex) > self.minHeap[currentIndex]:
            self.swap(currentIndex,self.getParentIndex(currentIndex))
            self.recursiveUpHeap(self.getParentIndex(currentIndex))
    
    def recursiveDownHeap(self,currentIndex):
        minIndex = currentIndex
        if self.hasLeftchild(currentIndex) and self.getLeftchild(currentIndex) < self.minHeap[minIndex]:
            minIndex = self.getLeftChildIndex(currentIndex)

        if self.hasRightChild(currentIndex) and self.getRightChild(currentIndex) < self.minHeap[minIndex]:
            minIndex = self.getRigtChildIndex(currentIndex)
        
        if minIndex != currentIndex:
            self.swap(currentIndex,minIndex)
            self.recursiveDownHeap(minIndex)
            
            

mh = MinHeap()

mh.insert(6)
mh.insert(4)
mh.insert(2)
mh.insert(1)
mh.insert(10)

print("After Inserts: ------------")
print(mh.minHeap)

mh.removeMin()

print("After Remove-----------")
print(mh.minHeap)



        




    