class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = dict()
        for strings in strs:
            sorted_strings = sorted(strings)
            joined_string = ''.join(sorted_strings)
            if joined_string in anas:
                anas[joined_string].append(strings)
            else: anas[joined_string] = [strings]
        return list(anas.values())