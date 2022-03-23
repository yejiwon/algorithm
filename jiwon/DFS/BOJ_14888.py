import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxVal = -1e9
minVal = 1e9


def dfs(level, now):
    global minVal, maxVal, add, sub, mul, div
    if level == n:
        maxVal = max(maxVal, now)
        minVal = min(minVal, now)

    else:
        if add > 0:
            add -= 1
            dfs(level + 1, now + nums[level])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(level + 1, now - nums[level])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(level + 1, now * nums[level])
            mul += 1
        if div > 0:
            div -= 1
            dfs(level + 1, now / nums[level])
            div += 1


dfs(1, nums[0])
print(maxVal)
print(minVal)
