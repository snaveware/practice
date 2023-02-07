class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestString = ""
        currentString = ""
        i = 0

        while len(s) > len(longestString):
            while i < len(s): 
                print("current: ", currentString)
                currentString += s[i]
                if self.isPalindrome(currentString) and len(currentString) > len(longestString):
                    longestString = currentString
                i += 1
            
            i = 0
            s = s[1:]
            currentString = ""
        
        print("longest: ",longestString)
            
        
        return longestString
        
    def isPalindrome(self,s: str):
        left = ""
        right = ""
        size = len(s)
        middle = size//2

        if size % 2 == 0:
            left = s[:middle]
            right = s[middle:]
        else: 
            left = s[:middle+1]
            right = s[middle:]
        
        right = right[::-1]

        return left == right 


answer = Solution().longestPalindrome("aakcaackaa") 

print(answer)
