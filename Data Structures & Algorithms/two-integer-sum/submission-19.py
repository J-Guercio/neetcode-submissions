class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        got = dict()
        for i,x in enumerate(nums):
            complament = target - x
            if complament in got:
                return[got[complament],i]
            else:
                got[x] = i