class Solution:
    def countSubstrings(self, s: str) -> int:
        resStr = 0

        def expand(l, r):
            nonlocal resStr
            while l >= 0 and r < len(s) and s[l] == s[r]:
                resStr += 1
                l -= 1
                r += 1
            return resStr
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return resStr