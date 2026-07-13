class Solution:
    def trap(self, height: List[int]) -> int:
        h_length = len(height)
        maxWater = 0
        left = 0
        right = h_length-1
        leftMax , rightMax = 0 , 0
        while left < right:
            if height[left] <= height[right]:
                leftMax = max(leftMax,height[left])
                maxWater += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax,height[right])
                maxWater += rightMax - height[right]
                right -= 1
        return maxWater