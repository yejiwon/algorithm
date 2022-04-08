class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                added = nums[i] + nums[start] + nums[end]
                
                if added < 0:
                    start += 1
                
                if added > 0:
                    end -= 1
                
                if added == 0:
                    arr = [nums[i], nums[start], nums[end]]
                    result.append(arr)
                    
                    end -= 1
                    
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
            
        return result


"""
added == 0 일 때 
result에 중복이 안 생기게 하려고 해당 arr가 이미 있는지 arr in result로 판별을 했더니 runtime이 5929 ms	가 나와서
그 부분 바꾸는 건 찾아보았다

"""