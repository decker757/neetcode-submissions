class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = 0
            numbers[num] += 1
        print(numbers)
        for k,v in numbers.items():
            if v > 1:
                return True
        return False