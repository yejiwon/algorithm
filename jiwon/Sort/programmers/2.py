# 가장 큰 수
# 정수를 이어붙여 가장 큰 수 만들기

import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(comparator), reverse=True)
    return ''.join(numbers)


if __name__ == "__main__":
    print(solution([3, 30, 34, 5, 9]))


# 첫번째 인수가 작으면 음수, 같으면 0, 크면 양수를 반환
# def numeric_compare(x, y):
#     return x - y
# sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(numeric_compare))
# // [1, 2, 3, 4, 5]