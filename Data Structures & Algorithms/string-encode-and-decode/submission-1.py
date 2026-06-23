class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = list()
        i = 0
        while i < len(s):
            j = s.find('#',i)
            lenth = int(s[i:j])
            decoded_strs.append((s[j+1 : j+1+lenth]))
            i = j + 1 + lenth
        return decoded_strs

