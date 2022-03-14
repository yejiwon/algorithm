class Solution:
    def longestPalindrome(self, s: str) -> int:
        wordCounts = collections.Counter(s)
        length = 0
        isOddExist = False
        for value in wordCounts.values():
            length += (value // 2) * 2
            if value % 2 == 1:
                isOddExist = True
        if isOddExist:
            length += 1
        return length