class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for i in strs:
            sortedStr = sorted(i)
            joinedStr = ''.join(sortedStr)
            if joinedStr in anas:
                anas[joinedStr].append(i)
            else:
                anas[joinedStr] = [i]
        return list(anas.values())