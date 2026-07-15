class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        leftMax,rightMax = 0,0
        maxWater = 0
        while left < right:
            leftRetainer = height[left]
            rightRetainer = height[right]
            if leftRetainer <= rightRetainer:
                leftMax = max(leftRetainer,leftMax)
                maxWater += leftMax - leftRetainer
                left +=1
            elif rightRetainer < leftRetainer:
                rightMax = max(rightRetainer,rightMax)
                maxWater += rightMax - rightRetainer
                right -= 1
        return(maxWater)