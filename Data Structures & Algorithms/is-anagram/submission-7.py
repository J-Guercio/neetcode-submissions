class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sD = dict()
        tD = dict()
        for i in s:
            sD[i] = sD.get(i,0) + 1
        for x in t:
            tD[x] = tD.get(x,0) + 1
        return tD == sD