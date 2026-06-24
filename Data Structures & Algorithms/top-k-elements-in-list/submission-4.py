class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i,0) + 1
        sortedCounter = sorted(counter.items(),key=lambda item:item[1], reverse=True)
        final = list()
        for j in range(k):
            final.append(sortedCounter[j][0])
        return final
        