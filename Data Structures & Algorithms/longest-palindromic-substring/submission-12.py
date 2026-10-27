class Solution:
    def longestPalindrome(self, s: str) -> str:
        startingIdx = 0
        resLen = 0

        def expand(l, r):
            nonlocal resLen, startingIdx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                windowLen = r - l + 1
                if windowLen > resLen:
                    startingIdx = l
                    resLen = windowLen

                l -= 1
                r += 1
            
            
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[startingIdx: startingIdx + resLen]