class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        n = len(s)
        m = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m):
            for j in range(-1, n):
                if j == -1:
                    if p[i] == "*":
                        dp[i+1][j+1] = dp[i][j+1]
                    continue
                if p[i].isalpha():
                    if p[i] == s[j]:
                        dp[i+1][j+1] = dp[i][j]
                elif p[i] == "?":
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        return dp[-1][-1]


"""
dp로 이전 index까지 매칭이 잘되었는지 확인
모르겠어서 유튜브 해설 영상 참고ㅠ

"""
