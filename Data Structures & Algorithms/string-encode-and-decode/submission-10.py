class Solution:

    def encode(self, strs: List[str]) -> str:
      encodedStr = ''
      for i in strs:
        encodedStr += str(len(i)) + '#'+ i
      return encodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        final = list()
        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            word = s[j+1:length+1+j]
            final.append(word)
            i = j + length + 1

        return final


