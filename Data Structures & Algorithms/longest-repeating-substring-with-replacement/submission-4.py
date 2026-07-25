class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l, max_length = 0, 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            window_size = r - l + 1

            if window_size - d[max(d, key=d.get)] <= k:
                max_length = max(max_length, window_size)
            else:
                d[s[l]] -= 1
                l += 1
        
        return max_length
