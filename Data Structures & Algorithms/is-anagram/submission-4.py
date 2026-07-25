class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for c in s:
            if c in freq_s:
                freq_s[c] += 1
            else:
                freq_s[c] = 1
        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1
        
        for key in freq_s.keys():
            if key not in freq_t:
                return False
            elif freq_t[key] != freq_s[key]:
                return False
        
        for key in freq_t.keys():
            if key not in freq_s:
                return False
            elif freq_t[key] != freq_s[key]:
                return False
                
        return True
        
        