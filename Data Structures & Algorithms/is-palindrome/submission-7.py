class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        reversed_s = ""
        
        for ch in s.strip():
            if ch.isalnum():
                cleaned_s += ch.lower()
        
        for i in range(len(cleaned_s) - 1, -1, -1):
            reversed_s += cleaned_s[i]
        
        return reversed_s == cleaned_s
        
        
            