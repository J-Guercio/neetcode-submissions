class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        some = dict()
        for i in strs:
            m = sorted(i)
            joinedM = ''.join(m)
            if joinedM in some:
                some[joinedM].append(i)
            else: some[joinedM] = [i]
        return list(some.values()) 
        