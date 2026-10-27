class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        max_count = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            windowLen = r - l + 1
            max_count = max(max_count, freq[s[r]])

            if windowLen - max(freq.values()) <= k:
                res = max(res, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res