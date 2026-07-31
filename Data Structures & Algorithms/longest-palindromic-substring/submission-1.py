class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    resLen = max(resLen, len(s[i:j+1]))
                    if len(s[i:j+1]) == resLen:
                        res = s[i:j+1]
        
        return res