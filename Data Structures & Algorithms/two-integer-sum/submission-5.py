class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            someDict = dict()
            for i,x in enumerate(nums):
                complament = target - x
                if complament in someDict:
                    return [someDict[complament],i]
                someDict[x] = i