class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = set()
        for i,x in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                TSum = x + nums[left] + nums[right]
                if TSum < 0: left += 1
                elif TSum > 0: right -= 1
                elif TSum == 0:
                    sums.add(tuple([x,nums[left],nums[right]]))
                    left+=1
        return(list(sums))