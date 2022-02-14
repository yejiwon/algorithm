def numberOfWaysToMakeChange(n, coins):
    ways = [0 for _ in range(n+1)]  # coins로 값 n을 만들 수 있는 방법
    ways[0] = 1

    for coin in coins:
        for amount in range(1, n+1):
            if coin <= amount:
                ways[amount] += ways[amount - coin]

    return ways[n]
