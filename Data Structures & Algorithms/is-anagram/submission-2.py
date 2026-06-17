class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sDict = dict()
        tDict = dict()
        for n in s:
            sDict[n] = sDict.get(n,0) + 1
        for n in t:
            tDict[n] = tDict.get(n,0) + 1
        return sDict == tDict

        