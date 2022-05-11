def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    zeros = 0
    
    for num in lottos:
        if num == 0:
            zeros += 1
        else:
            break
    
    min_coincide = len(set(lottos) & set(win_nums))
    max_coincide = zeros + min_coincide
    
    min_rank = 7-min_coincide if min_coincide > 0 else 6 
    max_rank = 7-max_coincide if max_coincide > 0 else 6
    
    answer = [max_rank, min_rank]
    
    return answer