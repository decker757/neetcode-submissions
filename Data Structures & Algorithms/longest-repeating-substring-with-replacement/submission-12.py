class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0
        for r in range(len(s)):
            ch = s[r]
            freq[ch] = freq.get(ch, 0) + 1
            maxValue = max(freq.values())
            if r - l + 1 - maxValue <= k:
                res = max(res, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1

        return res

