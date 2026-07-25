class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""

        n = len(s)

        for ch in s:
            if ch.isalnum():
                filtered_s += ch.lower()

        return True if filtered_s == filtered_s[::-1] else False