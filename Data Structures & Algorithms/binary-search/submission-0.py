class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        
        while right - left > 1:
            middle = (left+right)//2
            if nums[middle] > target:
                right = middle 
            elif nums[middle] < target:
                left = middle 
            else:
                return middle
        return -1
