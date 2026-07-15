class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ''.join(char for char in s if char.isalnum())
        m = m.lower()
        reverseM = m[::-1]
        return m == reverseM