class Solution():
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        converted = list()
        skip = False

        for i in range(len(s)) :
            print(i)
            if skip: 
                skip = False
                continue
            if s[i] == 'M':
                converted.append(1000)
            if s[i] == 'D':
                converted.append(500)
            if s[i] == 'C':
                if i+1 < len(s) and s[i+1] == "D":
                    converted.append(400)
                    skip = True
                elif i+1 < len(s) and s[i+1] == "M":
                    converted.append(900)
                    skip = True
                else:
                    converted.append(100)
            if s[i] == "L":
                converted.append(50)
            if s[i] == "X":
                if i+1 < len(s) and s[i+1] == "L":
                    converted.append(40)
                    skip = True
                elif i+1 < len(s) and s[i+1] == "C" :
                    converted.append(90)
                    skip = True
                else:
                    converted.append(10)
            if s[i] == "V":
                converted.append(5)
            if s[i] == "I":
                if i+1 < len(s) and s[i+1] == "V" :
                    converted.append(4)
                    skip = True
                elif i+1 < len(s) and s[i+1] == "X" :
                    converted.append(9)
                    skip = True
                else:
                    converted.append(1)
    
        answer = 0
        for value in converted:
            answer += value
        
        return answer

answer = Solution().romanToInt("MX")

print("answer= ",answer)
