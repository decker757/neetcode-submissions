class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for n in hashSet:
            if n - 1 not in hashSet:
                length = 1
                while (n + length) in hashSet:
                    length += 1
                longest = max(longest, length)
        
        return longest

        
        

        
