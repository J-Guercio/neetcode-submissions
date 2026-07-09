class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
          sumLR = numbers[left] + numbers[right]
          if sumLR == target:
            return[left+1,right+1]
          if sumLR < target:
            left = left + 1
          if sumLR > target:
            right = right - 1
         
        