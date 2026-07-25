class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        if len(s) != len(t):
            return False

        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1
        
        for c in t:
            if c not in freq_s:
                return False
            freq_s[c] -= 1
            if freq_s[c] < 0:
                return False
        return True
        