class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i,x in enumerate(nums):
                for j,k in enumerate(nums[i+1:], i +1):
                    if x + k == target:
                        return [i,j]