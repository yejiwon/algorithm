class Solution: 
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

"""
한 10개정도 직접해봤는데 짝수로 시작하는 경우에만 이겨서 한번 고민을 해봤다.
n이 홀수가 되면 n의 인수도 모두 홀수라 다음 사람에겐 짝수를 넘겨줘 기회가 된다.
"""