class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])
            window_length = r - l + 1

            if window_length - maxf <= k:
                res = max(res, window_length)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res