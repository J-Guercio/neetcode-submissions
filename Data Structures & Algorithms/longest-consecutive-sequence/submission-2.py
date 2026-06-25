class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        nums.sort()
        count = 1
        highestCount = 1
        for i,x in enumerate(nums):
            prev = nums[i-1]
            target = prev + 1
            if x == target:
                count = count + 1
                if highestCount < count:
                    highestCount = count
            if x == nums[i-1]:
                continue
            if i == 0:
                continue
            if x != target:
                count = 1
        return highestCount