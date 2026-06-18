class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i,n in enumerate(nums):
            counter[n] = counter.get(n,0) + 1
        sortedCounter = (sorted(counter.items(), key=lambda item: item[1], reverse=True))
        final = list()
        for i in range(k):
            final.append(sortedCounter[i][0])
        return final