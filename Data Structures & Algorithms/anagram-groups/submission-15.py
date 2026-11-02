class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for x in strs:
            m = sorted(x)
            joined_sorted = ''.join(m)
            if joined_sorted in anas:
                anas[joined_sorted].append(x)
            else:
                anas[joined_sorted] = [x]
        return (list(anas.values()))