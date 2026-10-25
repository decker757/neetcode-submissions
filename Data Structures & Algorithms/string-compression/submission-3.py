class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1

        for r in range(1, len(chars)):
            if chars[r] == chars[r - 1]:
                count += 1
            else:
                chars[write] = chars[r - 1]
                write += 1

                if count > 1:
                    for ch in str(count):
                        chars[write] = ch
                        write += 1
                count = 1
        
        chars[write] = chars[-1]
        write += 1
        if count > 1:
            for ch in str(count):
                chars[write] = ch
                write += 1
        return write