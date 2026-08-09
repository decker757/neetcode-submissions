class Solution:
    def firstUniqChar(self, s: str) -> int:
        charSet = {}

        for ch in s:
            charSet[ch] = charSet.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if charSet[ch] == 1:
                return i
        
        return -1