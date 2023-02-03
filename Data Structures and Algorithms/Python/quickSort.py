import random
def quickSort(values):
    size = len(values)
    if not values or size <=1:
        return values

    pivotIndex = random.randint(0,size-1)
    pivot = values[pivotIndex]

    values.pop(pivotIndex)

    lessValues = []
    greaterValues = []

    for value in values:
        if value <=pivot:
            lessValues.append(value)
        else:
            greaterValues.append(value)

    lessValues = quickSort(lessValues) 
    greaterValues = quickSort(greaterValues)

    values = lessValues
    values.append(pivot)
    values.extend(greaterValues)
    return  values
    


values = [88,7,5,4,45,35,75,9]

sorted = quickSort(values)

print(sorted)


