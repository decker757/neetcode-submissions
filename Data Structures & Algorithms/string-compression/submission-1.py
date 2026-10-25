class Solution:
    def compress(self, chars: List[str]) -> int:
        w = l = 0

        for r in range(len(chars) + 1):
            if r == len(chars) or chars[r] != chars[l]:
                chars[w] = chars[l]
                w += 1

                count = r - l
                if count > 1:
                    for d in str(count):
                        chars[w] = d
                        w += 1
                l = r
        
        return w
                