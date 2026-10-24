class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = {}

        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if freq_map.get(ch) == 1:
                return i
        
        return -1
         