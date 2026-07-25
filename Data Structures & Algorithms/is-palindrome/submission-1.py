class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""

        for ch in s:
            if ch.isalnum():
                ss += ch.lower()
        if ss != ss[::-1]:
            return False
        else:
            return True