class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        sortedSeen = sorted(seen.items(), key=lambda item:item[1],reverse=True)
        final = list()
        for i in range(k):
            final.append(sortedSeen[i][0])
        return final