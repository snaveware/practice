def mergeSort(values):
    size = len(values)
    if not values or size <=1:
        return values
    
    mid = size//2

    print("values: ",values)

    leftList = values[:mid]
    rightList = values[mid:]

    leftList = mergeSort(leftList)

    rightList = mergeSort(rightList)

    sorted = merge(leftList,rightList)

    print("sorted: ",sorted)

    return sorted


def merge(leftList,rightList):
    leftIndex = 0
    rightIndex = 0
    leftSize = len(leftList)
    rightSize = len(rightList)
    sorted = []
    while leftIndex < leftSize and rightIndex < rightSize:
        if leftList[leftIndex] < rightList[rightIndex]:
            sorted.append(leftList[leftIndex])
            leftIndex +=1
        else:
            sorted.append(rightList[rightIndex])
            rightIndex +=1
        
    while leftIndex < leftSize:
        sorted.append(leftList[leftIndex])
        leftIndex += 1
    

    while rightIndex < rightSize:
        sorted.append(rightList[rightIndex])
        rightIndex +=1
    
    if leftSize == 2 and rightSize == 2:
        print("double: ",leftList,rightList,sorted)
    return sorted


values = [88,7,5,4,45,35,75,4]

sorted = mergeSort(values)

print(sorted)