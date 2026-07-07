class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for i in strs:
            encodedString += str(len(i)) + '#' + i
        return encodedString
    def decode(self, s: str) -> List[str]:
        strlen = len(s)
        i = 0
        final = list()
        while i < strlen:
            j = s.find('#',i)
            length = s[i:j]
            wordLength = int(int(j) + int(length))
            word = s[j+1:wordLength+1]
            final.append(word)
            i = wordLength + 1
        return final

