# https://programmers.co.kr/learn/courses/30/lessons/60058
# 어떤 단계로 되돌아가기 -> 재귀함수

LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"

# 균형잡힌 괄호 문자열인지 확인


def isBalancedString(string):
    leftCount = 0
    rightCount = 0

    for s in string:
        if s == LEFT_PARENTHESIS:
            leftCount += 1
        else:
            rightCount += 1
        if leftCount == rightCount:
            return leftCount + rightCount


# 올바른 괄호 문자열인지 확인
def isRightString(string):
    count = 0
    if string[0] == LEFT_PARENTHESIS:
        for s in string:
            if s == LEFT_PARENTHESIS:
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return True
    else:
        return False

# 전체 프로세스


def solution(input):
    if len(input) == 0:
        return input

    idx = isBalancedString(input)
    u = input[:idx]
    v = input[idx:]

    if isRightString(u):
        ans = u + solution(v)
        return ans
    else:
        ans = LEFT_PARENTHESIS + solution(v) + RIGHT_PARENTHESIS
        u = u[1:-1]
        for i in u:
            if i == LEFT_PARENTHESIS:
                ans += RIGHT_PARENTHESIS
            else:
                ans += LEFT_PARENTHESIS
        return ans


if __name__ == "__main__":
    solution("()))((()")
