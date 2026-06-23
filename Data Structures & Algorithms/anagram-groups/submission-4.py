class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        for i in strs:
            m = sorted(i)
            joinedM = ''.join(m)
            if joinedM in seen:
                seen[joinedM].append(i)
            else:
                seen[joinedM] = [i]
        return list(seen.values())
