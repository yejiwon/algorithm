class Solution(object):
    def countBits(self, n):        
        dp = [0] * (n+1)

        for i in range(1, n+1):
            share = i // 2
            if i%2 == 0:
                dp[i] = dp[share]
            else:
                dp[i] = dp[share] + 1
        
    
        return dp
"""
다른 사람 풀이

class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i-offset] + 1
            
        return dp
"""