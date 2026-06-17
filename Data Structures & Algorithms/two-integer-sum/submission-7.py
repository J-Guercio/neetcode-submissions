class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        some = dict()
        for i,n in enumerate(nums):
            complament = target - n
            if complament in some:
                return [some[complament],i]
            some[n] = i