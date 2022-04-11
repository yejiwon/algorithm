def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    brokenCnt = lottos.count(0)
    sameCnt = 0

    for x in win_nums:
        for x in lottos:
            sameCnt += 1

    return rank[brokenCnt + sameCnt], rank[sameCnt]
