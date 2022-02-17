class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] not in t:
                return False
            t = t[t.index(s[i]) + 1 :]
        return True