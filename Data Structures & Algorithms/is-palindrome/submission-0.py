class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr= ''

        for ch in s:
            if ch.isalnum():
                newStr += ch.lower()
        
        if newStr == newStr[::-1]:
            return True
        return False