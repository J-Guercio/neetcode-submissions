class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i,x in enumerate(nums):
            complament = target - x
            if complament in seen:
                return[seen[complament], i]
            seen[x] = i
