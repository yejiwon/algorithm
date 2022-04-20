class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for i in arr1:
            for j in arr2:
                distance = abs(i - j)
                if distance <= d:
                    answer += 1
                    break
        return len(arr1) - answer
#         arr2.sort()
#         answer = 0
#         for num in arr1:       
#             left, right = 0, len(arr2)
#             while left < right:
#                 mid = (left + right) // 2
#                 distance = arr2[mid] - num
#                 if -d <= distance <= d:
#                     break
#                 if distance > d:
#                     right = mid
#                 else:
#                     left = mid + 1
#             else:
#                 answer += 1
#         return answer

"""
카테고리에 sorting과 binary search가 있어서 바이너리 서치로도 풀어봤다(주석된 코드)
근데 실제로 해보니까 막상 돌려보니 for문 도는게 더 빨랐다
leetcode에 있는 테스트케이스가 어쩌다 보니 운 좋게 그런 케이스들만 있는걸까?
"""