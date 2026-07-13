class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for x in strs:
            encoded_string += str(len(x)) + '#' + x
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decodedList = list()
        i = 0 
        EncodeLength = len(s)
        while i < EncodeLength:
            j = s.find('#',i)
            lengthOfWord = int(s[i:j])
            word = s[j+1:j+lengthOfWord+1]
            decodedList.append(word)
            i = j + lengthOfWord + 1
        return(decodedList)

