class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = ""

        for ch in s:
            if ch.isalnum():
                s_filtered += ch.lower()
        
        return s_filtered == s_filtered[::-1]