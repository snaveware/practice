class Solution:
    def kWeakestRows(self, mat, k: int):
        soldiers = list()
        for row in mat:
            noOfSoldiers = 0
            for value in row:
                if value == 1:
                    noOfSoldiers += 1
            
            soldiers.append(noOfSoldiers)

        print("soldiers unsorted: ",soldiers)
        sortedRows = list()
        for i in range(len(soldiers)):
            sortedRows.append(i)
            
        print("Rows B4 Sort: ",sortedRows)
        
        for i in range(len(soldiers)):
            j=i
            while j>0 and soldiers[j-1] > soldiers[j]:
                temp = soldiers[j-1]
                soldiers[j-1] = soldiers[j]
                soldiers[j] = temp
                temp2 = sortedRows[j-1]
                sortedRows[j-1] = sortedRows[j]
                sortedRows[j] = temp2
                j -= 1
        
        print("soldiers: ",soldiers)
        print("sortedRows: ", sortedRows)

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

Solution().kWeakestRows(mat,3)