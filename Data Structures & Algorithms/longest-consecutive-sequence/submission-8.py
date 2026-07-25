class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        current = 1

        sortedNums = sorted(set(nums))
        n = len(sortedNums)

        if n == 0:
            return 0

        for i in range(1, n):
            if abs(sortedNums[i] - sortedNums[i-1]) == 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)

        return longest