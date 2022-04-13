# 전화번호 목록
def solution(phoneBook):
    answer = True
    hashMap = {}
    for phone in phoneBook:
        hashMap[phone] = 1

    for phone in phoneBook:
        tmp = ''
        for num in phone:
            tmp += num
            if tmp in hashMap and tmp != phone:
                answer = False
                break

    return answer


if __name__ == "__main__":
    print(solution(["123", "456", "789"]))