class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums.sort()
        for i in range(len(nums)):
          x = nums[i]
          right = len(nums) - 1
          left = i + 1
          while left < right:
            y = nums[left]
            z = nums[right]
            sumT = x+y+z
            if sumT == 0:
              sol.add(tuple([x,y,z]))
              left = left + 1
            elif sumT > 0:
              right = right - 1
            elif sumT < 0:
              left = left + 1
        return list(sol) 