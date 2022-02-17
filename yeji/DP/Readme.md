### Dynamic programming
---

복잡한 하난의 문제를 여러 하위 문제들로 나누고, 각각의 결과를 저장한 후 해당 문제에 대한 중복 컴퓨팅을 제거하여 효율성을 개선하는 방법


**같은 input에 대해 반복되는 호출을 하는 솔루션을 만났을 때 DP로 최적화 가능**

#### DP의 두가지 방법
> ### Tabulation (bottom-up)
>  작은 값에서부터 차례로(= tabulation) 값들을 구하고, 재사용 해 나가며 결과값을 구할 수 있음
>
> Fibonacci sequence pseudocode
>
>```
>F = array of len(n+1)
>F[0] = 0
>F[1] = 1
>for i from 2 to n:
>   F[i] = F[i-1] + F[i-2]
>```

> ### Memoization (top-down)
>
> 결과값에 먼저 접근하려는 시도를 하고, 해당 값에 가까운 값을 DP에서 찾아나가며 중복된 값을 사용하거나 메모
>
> Fibonacci sequence pseudocode
>```memo = hashmap
>Function F(integer i):
>    if i is 0 or 1: 
>        return i
>    if i doesn't exist in memo:
>        memo[i] = F(i - 1) + F(i - 2)
>    return memo[i]
>```

#### DP를 사용하는 경우
1. 어떤 것의 최적값(혹은 최소, 최대) 또는 무언가를 수행하는데 경우의 수를 요구 ex. 최소 비용, 최대 이익, 가장 긴 것...
2. 다음의 결과값이 이전 결과값에 달려있음 - DP와 greedy 를 구분하는 중요한 특성
3. 해결하고자 하는 복잡한 문제가 여러개의 하위 문제들로 나뉘며 하위 문제들 사이엔 중복되는 문제가 존재
4. main problem의 최적해가 하위 문제들의 최적해들의 집합으로 이루어진다. ex. 경유해서 길찾기 - 서울 (대전) 부산 순으로 가야하는 경우 `(1)서울에서 대전에 가는법` 과 `(2)대전에서 부산을 가는 법` 이렇게 두가지로 나뉘고 최적해는 (1)과 (2) 각각의 최적해의 합과 같음. 