class Solution:
    def isIncludeChar(self, strs, char, i):
        for word in strs:
            if word[i] != char:
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        prefix = ''
        strs.sort(key = lambda x:len(x))
        word = strs[0]
        
        for i in range(len(word)):
            currentChar = word[i]
            if self.isIncludeChar(strs, currentChar, i):
                prefix += currentChar
            else:
                return prefix
        return prefix
        
        