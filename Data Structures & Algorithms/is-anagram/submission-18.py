class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}

        if len(s) != len(t):
            return False

        for ch in s:
            s_map[ch] = 1 + s_map.get(ch, 0)
        
        for ch in t:
            if ch in s_map:
                s_map[ch] -= 1
        
        for k in s_map:
            if s_map[k] > 0:
                return False
        
        return True
        