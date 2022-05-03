def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    report = set(report)

    for r in report:
        reports[r.split()[1]] += 1

    for r in report:
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

"""
dictionary의 key 값을 신고자로 하니까 타임아웃이 났다.
그래서 반대로 신고받은 사람을 key값으로 하니 훨씬 빨라졌다.
"""