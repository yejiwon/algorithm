class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n == 1:
            return s
        
        for i in range(2, n+1):
            j = 0
            temp = ""
            curr = ""
            count = 0
            
            while j < len(s):
                if curr == "":
                    curr = s[j]
                    count = 1
                    j += 1
                elif curr == s[j]:
                    count += 1
                    j += 1
                else:
                    temp += str(count) + curr
                    curr=""
                    count = 0
        
            temp += str(count) + curr
            s=temp
        return s