class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            windowLen = r - l + 1

            if windowLen - max(freq.values()) <= k:
                res = max(res, windowLen)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res