# 기능 개발
# 순서대로 배포

import math

def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        remain = math.ceil((100 - p)/s)
        if len(Q) == 0 or Q[-1][0] < remain:
            Q.append([remain, 1])
        else:
            Q[-1][1] += 1

    return [q[1] for q in Q]


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))