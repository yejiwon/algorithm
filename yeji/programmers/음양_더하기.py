def solution(absolutes, signs):
    answer = 0
    
    for index in range(len(signs)):
        num = absolutes[index] if signs[index] else absolutes[index] * -1
        answer += num
    return answer
