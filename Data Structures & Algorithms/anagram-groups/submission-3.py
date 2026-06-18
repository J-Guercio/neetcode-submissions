class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for x in strs:
            m = sorted(x)
            joinedM = ''.join(m)
            if joinedM in anas:
                anas[joinedM].append(x)
            else:
                anas[joinedM] = [x]
        return list(anas.values())       