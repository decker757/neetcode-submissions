class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, res = 0, 0

        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            winLen = i - l + 1

            if winLen - freq[max(freq, key=freq.get)] <= k:
                res = max(res, winLen)
            else:
                freq[s[l]] -= 1
                l += 1

        return res
            

        