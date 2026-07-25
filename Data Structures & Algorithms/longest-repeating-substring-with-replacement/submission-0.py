class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        charSet = set(s)

        for ch in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == ch:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == ch:
                        count -= 1
                    l += 1

                result = max(result, r - l + 1)
        return result
