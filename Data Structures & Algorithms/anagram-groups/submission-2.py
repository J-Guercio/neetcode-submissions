class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for i in strs:
            m = sorted(i)
            joinedM = ''.join(m)
            if joinedM in anas:
                anas[joinedM].append(i)
            else:
                anas[joinedM] = [i]
        return list(anas.values())