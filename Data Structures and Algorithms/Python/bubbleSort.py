def bubbleSort (values):
    for i in range(len(values)-1):
        for j in range(len(values)-1):
            if values[j] > values[j+1]: 
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp
    
    return values

values = [1,5,35,6,4,32,9,67]

sorted = bubbleSort(values)

print(sorted)