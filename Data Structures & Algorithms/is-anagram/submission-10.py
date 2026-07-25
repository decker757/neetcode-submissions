class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for ch in s:
            if ch not in s_map:
                s_map[ch] = 1
            else:
                s_map[ch] += 1

        for ch in t:
            if ch not in t_map:
                t_map[ch] = 1
            else:
                t_map[ch] += 1
        
        if t_map == s_map:
            return True
        return False