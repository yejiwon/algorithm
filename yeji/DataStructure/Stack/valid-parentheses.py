class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { '}': '{', ']': '[', ')': '(' }
        stack = []
        
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack