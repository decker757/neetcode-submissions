class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1
        
        return all(val == 0 for val in d.values())