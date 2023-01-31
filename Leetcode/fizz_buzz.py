class Solution:
    def fizzBuzz(self, n: int) :
        returnList = list()
        for i in range(n+1):
            if i==0:
                continue
            elif i%15 == 0:
                returnList.append("FizzBuzz")
            elif i%3 == 0:
                returnList.append("Fizz")
            elif i%5 == 0:
                returnList.append("Buzz")
            else:
                returnList.append(str(i))
        
        return returnList
