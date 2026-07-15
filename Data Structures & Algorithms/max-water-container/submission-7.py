class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVol = 0
        while left < right:
            leftRetainer = heights[left]
            rightRetainer = heights[right]
            length = right - left
            totalVol = length * min(leftRetainer,rightRetainer)
            if totalVol > maxVol: maxVol = totalVol
            if leftRetainer < rightRetainer: left+=1
            elif rightRetainer < leftRetainer: right-=1
            else: left+=1
        return maxVol