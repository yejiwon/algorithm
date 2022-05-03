class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 :
            return 0
        
        index = 0
        maxHeight = height[index]
        
        for i in range(1, len(height)):
            if height[i] > maxHeight:
                maxHeight = height[i]
                index = i
                
        
        leftMax = height[0]
        rightMax = height[-1]
        
        area = 0
        
        for i in range(0, index):
            if height[i] > leftMax:
                leftMax = height[i]
            else:
                area += (leftMax - height[i])
                
                
        for i in range(len(height)-1, index, -1):
            if height[i] > rightMax:
                rightMax = height[i]
            else:
                area += (rightMax - height[i])
                
        return area