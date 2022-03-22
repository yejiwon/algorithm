class Solution:
    def generateParenthesisUtil(self, left, right, temp, result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left > 0:
            self.generateParenthesisUtil(left-1, right, temp+'(', result)
        if right > left:
            self.generateParenthesisUtil(left, right-1, temp+')', result)
    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesisUtil(n,n,"",result)
        return result