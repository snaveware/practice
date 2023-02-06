class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubString = ""
        if len(s) <= 1:
            return len(s)
        currentString = s[0]

        for i in range(1,len(s)):
            print("index:", i)
            if s[i] not in currentString:
                currentString += s[i]
                print("not in: ",s[i])
                if len(currentString) > len(longestSubString):
                    longestSubString = currentString
            else:
                if len(currentString) > len(longestSubString):
                    longestSubString = currentString
                indexOfChar = currentString.index(s[i])
                print("indexOfChar",indexOfChar)
                currentString = currentString[indexOfChar+1:]
                currentString += s[i]

            
            print( "current String: ",currentString)
            print("longest String: ",longestSubString)
        
        return len(longestSubString)



answer = Solution().lengthOfLongestSubstring("aab")

print("answer: ",answer)