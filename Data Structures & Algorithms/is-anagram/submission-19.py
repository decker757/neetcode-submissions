class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}

        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        
        for ch in t:
            if ch not in s_map:
                return False
            elif s_map[ch] == 0:
                return False
            s_map[ch] -= 1
        
        for ch in s_map:
            if s_map[ch] > 0:
                return False
        
        return True