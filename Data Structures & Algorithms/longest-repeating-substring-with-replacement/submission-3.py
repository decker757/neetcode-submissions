class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l, res = 0, 0

        for r in range(len(s)):
            ch = s[r]
            d[ch] = 1 + d.get(ch, 0)

            window_size = r - l + 1
            max_f = d[max(d, key=d.get)]

            if window_size - max_f <= k:
                res = window_size
            else:
                d[s[l]] -= 1
                l += 1
        return res
