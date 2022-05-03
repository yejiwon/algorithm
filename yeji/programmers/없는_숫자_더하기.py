def solution(numbers):
    maxSum = sum([0,1,2,3,4,5,6,7,8,9])
    now = sum(numbers)
    answer = maxSum - now
    return answer