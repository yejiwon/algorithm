class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            width = right - left
            if (heights[left] > heights[right]):
                height = heights[right]
                right -= 1
            else:
                height = heights[left]
                left += 1
            area = max(area, width * height)
            
        return area 