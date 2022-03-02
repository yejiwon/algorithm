class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        subString = ''
        
        for i in range(len(s)):
            if s[i] in subString:
                subString = subString + s[i]
                subString = subString[subString.index(s[i])+1:]
            else:
                subString += s[i]
            maxLen = max(maxLen, len(subString))
        return maxLen