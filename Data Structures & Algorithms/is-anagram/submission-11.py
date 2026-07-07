class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = dict()
        tD = dict()
        for i in s:
            sD[i] = sD.get(i,0) + 1
        for i in t:
            tD[i] = tD.get(i,0) + 1
        return sD == tD    