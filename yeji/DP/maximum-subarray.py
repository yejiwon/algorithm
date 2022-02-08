class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        current = 0
        
        if len(nums) == 1:
            return nums[0]
        
        for n in nums:
            if current < 0:
                current = 0
            current += n
            maxSum = max(maxSum, current)
        
        return maxSum

# https://www.youtube.com/watch?v=5WZl3MMT0Eg 참고