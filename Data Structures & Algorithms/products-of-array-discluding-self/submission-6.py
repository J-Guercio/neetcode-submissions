class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = list()
        for i,x in enumerate(nums):
            product = 1
            for j,x in enumerate(nums):
                if j == i: continue
                else: product = product * x
            prods.append(product)
        return prods