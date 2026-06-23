class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decodedStrings = list()
        i = 0
        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            decodedStrings.append((s[j+1 : j+1+length]))
            i = j + 1 + length
        return decodedStrings

