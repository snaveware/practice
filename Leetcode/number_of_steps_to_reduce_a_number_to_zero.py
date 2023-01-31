class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while True:
            if num == 0:
                break
                
            steps += 1

            if num%2 == 0:
                num = num/2
            else:
                num -= 1
        
        return steps