class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        tDict = dict()
        sDict = dict()
        for l in t: tDict[l] = 1 + tDict.get(l,0)
        for l in s: sDict[l] = 1 + sDict.get(l,0)
        return tDict == sDict