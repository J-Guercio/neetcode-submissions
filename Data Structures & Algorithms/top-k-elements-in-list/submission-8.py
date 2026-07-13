class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        final = list()
        for x in nums:
            count[x] = count.get(x,0) + 1
        sortedCount = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for x in range(k):
            final.append(sortedCount[x][0])
        return final
