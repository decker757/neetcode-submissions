class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1

        for r in range(1, len(chars)):
            if chars[r] != chars[r - 1]:
                chars[write] = chars[r - 1]
                write += 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                count = 1
            else:
                count += 1
        
        chars[write] = chars[-1]
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
        return write
                