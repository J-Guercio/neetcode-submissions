class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for x in strs:
            m = sorted(x)
            joined = ''.join(m)
            if joined in anas:
                anas[joined].append(x)
            else:
                anas[joined] = [x]
        return list(anas.values())