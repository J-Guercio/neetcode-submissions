class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        for x in nums:
            numsRemoveI = nums[:]
            numsRemoveI.remove(x)
            prodOfNums = 1
            for j in numsRemoveI:
                prodOfNums = prodOfNums * j
            prods.append(prodOfNums)
        return prods