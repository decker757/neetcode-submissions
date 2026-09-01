class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStartingIdx = 0
        resLen = 0

        def expand(l, r):
            nonlocal resStartingIdx, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resStartingIdx = l
                l -= 1
                r += 1
            return resLen
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[resStartingIdx: resStartingIdx + resLen]
