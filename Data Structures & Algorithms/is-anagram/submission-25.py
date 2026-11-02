class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        tDict = dict()
        sDict = dict()
        for letter in s:
            sDict[letter] = 1 + sDict.get(letter, 0)
        for letter in t:
            tDict[letter] = 1 + tDict.get(letter,0)
        return tDict == sDict