class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            answer.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    answer[i].append(1)
                else:
                    answer[i].append(answer[i-1][j-1] + answer[i-1][j])
        return answer

"""
종종 for의 범위 설정을 잘못하는거 같다..
그래서 한 5번 틀린듯ㅜ
"""