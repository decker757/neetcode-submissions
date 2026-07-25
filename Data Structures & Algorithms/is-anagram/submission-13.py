class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        max_length = s_dict
        min_length = t_dict

        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            s_dict[ch] += 1
        
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 1
            t_dict[ch] += 1

        if len(t_dict) > len(s_dict):
            max_length = t_dict
            min_length = s_dict
        else:
            max_length = s_dict
            min_length = t_dict

        for k,v in max_length.items():
            if k not in min_length or t_dict[k] != s_dict[k]:
                return False
        return True
