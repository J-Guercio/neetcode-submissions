class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sDict = dict()
        tDict = dict()
        for i in s: sDict[i] = 1 + sDict.get(i,0)
        for j in t: tDict[j] = 1 + tDict.get(j,0)
        return sDict == tDict