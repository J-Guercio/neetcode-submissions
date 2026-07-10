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
            if heights[left] < heights[right]:
              left = left + 1
            elif heights[right] < heights[left]:
              right = right - 1
          elif heights[left] < heights[right]: left = left + 1
          elif heights[right] < heights[left]: right = right -1
          elif length == 1:
            if (min(heights[left],heights[right]) * length) > maxContain:
              maxContain = (min(heights[left],heights[right]) * length)
            left = left + 1
          elif heights[left] == heights[right]:
            if heights[left+1] > heights[right-1]:
              left = left + 1
            elif heights[left+1] < heights[right-1]:
              right = right - 1
            else: left = left + 1
              
            
        return maxContain