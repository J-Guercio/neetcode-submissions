class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final = list()
        for i in nums * 2:
            final.append(i)
        return final