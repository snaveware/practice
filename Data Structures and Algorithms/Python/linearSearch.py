def linearSearch(values,target):
    for i in range(len(values)):
        if values[i] == target:
            return i

values = [1,5,35,6,42,9,3,67]

index = linearSearch(values,6)

print(index)