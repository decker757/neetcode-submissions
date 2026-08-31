class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal res
                res += 1
                l -= 1
                r += 1
            return res
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return res