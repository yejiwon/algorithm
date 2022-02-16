class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        
        if n < 2:
            return nums[n]
        
        for i in range(2, n+1):
            if i % 2 == 0:
                nums.append(nums[i//2])
            else:
                index = i//2
                nums.append(nums[index] + nums[index+1])
        
        return max(nums)