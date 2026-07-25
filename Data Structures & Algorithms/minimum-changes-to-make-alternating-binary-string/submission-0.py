class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mismatch_start_zero = 0
        i = 0

        while i < n:
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:
                mismatch_start_zero += 1
            i += 1
        return min(mismatch_start_zero, n - mismatch_start_zero)