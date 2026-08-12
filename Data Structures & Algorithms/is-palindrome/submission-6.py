class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for ch in s:
            if ch.isalnum():
                cleaned_s += ch.lower()
        return cleaned_s == cleaned_s[::-1]