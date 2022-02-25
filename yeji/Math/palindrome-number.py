class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        reverseX = stringX[::-1]
        return stringX == reverseX

"""
이 풀이를 원한 문제는 아닌거 같다
"""