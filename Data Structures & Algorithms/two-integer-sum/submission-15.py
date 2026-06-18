class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = dict()
        for i,x in enumerate(nums):
            complament = target - x
            if complament in p:
                return[p[complament],i]
            else:
                p[x] = i