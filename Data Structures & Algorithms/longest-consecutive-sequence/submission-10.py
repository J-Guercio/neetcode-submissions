class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        maxCount = 0
        for i,x in enumerate(nums):
            if i == 0 or count == 0:
                prev = x
                count = count + 1
                if maxCount < count: maxCount = count
            if x == prev:
                if maxCount < count: maxCount = count
                continue
            if x == prev + 1:
                count = count + 1
                prev = x
                if maxCount < count: maxCount = count
                continue
            else:
                prev = x
                count = 1
        if count > maxCount: maxCount = count        
        return maxCount
