class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContain = 0
        ContainerLength = len(heights)
        left = 0
        right = ContainerLength - 1
        while left < right:
          length = right - left
          currentContainer = min(heights[left],heights[right]) * length
          if currentContainer > maxContain: 
            maxContain = currentContainer
          if heights[left] <= heights[right]: 
            left += 1 
          elif heights[right] < heights[left]: 
            right -= 1
        return maxContain