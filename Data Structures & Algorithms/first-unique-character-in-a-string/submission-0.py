class Solution:
    def firstUniqChar(self, s: str) -> int:
        charSet = {}

        for ch in s:
            charSet[ch] = charSet.get(ch, 0) + 1
        
        for k in charSet:
            if charSet[k] == 1:
                return s.index(k)
        
        return -1