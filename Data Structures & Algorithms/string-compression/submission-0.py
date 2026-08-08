class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0

        while r < len(chars):
            ch = chars[r]
            count = 0
            while r < len(chars) and chars[r] == ch:
                count += 1
                r += 1
            chars[l] = ch
            l += 1
            if count > 1:
                for d in str(count):
                    chars[l] = d
                    l += 1
        return l