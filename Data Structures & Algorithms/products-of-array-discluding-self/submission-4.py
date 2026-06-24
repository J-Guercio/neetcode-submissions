class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodsOrWhatEver = list()
        for i in nums:
            numsCopy = nums[:]
            numsCopy.remove(i)
            product = 1
            for j in numsCopy:
                product = product * j
            prodsOrWhatEver.append(product)
        return prodsOrWhatEver
        