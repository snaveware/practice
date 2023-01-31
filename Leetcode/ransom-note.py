class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        answer = True
        for letter in ransomNote:
          
            if letter in magazine:
                magazine = magazine.replace(letter,'',1)
                print("magazine: ",magazine)
            else:
                print("not in letter: ", letter)
                answer = False
                break
        
        print(answer)
        return answer


Solution().canConstruct("aa","ab")