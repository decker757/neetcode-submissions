class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            windowLen = r - l + 1
            highestFreq = max(freq.values())

            if windowLen - highestFreq <= k:
                res = max(res, windowLen)
            else:
                freq[s[l]] -= 1
                l += 1

        return res