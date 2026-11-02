class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for x in nums:
            if x in seen: return True
            else: seen[x] = x
        return False