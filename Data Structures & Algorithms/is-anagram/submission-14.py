class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 0
            s_dict[ch] += 1

        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            t_dict[ch] += 1
        
        for k in s_dict:
            if k not in t_dict:
                return False
            elif s_dict[k] != t_dict[k]:
                return False
        return True