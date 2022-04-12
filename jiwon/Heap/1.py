# 더 맵게
# 모든 음식 스코빌 지수를 K 이상으로 하기
import heapq as hq

def solution(scoville, K):
    scoville.sort()
    hq.heapify(scoville)
    cnt = 0
    while(True):
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1

        second = hq.heappop(scoville)
        new = first + second * 2
        hq.heappush(scoville, new)
        cnt += 1

    return cnt

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))