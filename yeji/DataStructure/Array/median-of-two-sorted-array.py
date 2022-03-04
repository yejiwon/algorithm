class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        sortedList = sorted(merged)
        
        length = len(merged)
        index = length // 2

        if length % 2 == 0:
            return (sortedList[index-1] + sortedList[index]) / 2
        return sortedList[index]

"""
median 정의 활용하는 방법도 알아보기
"""