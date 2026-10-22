class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr, used):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    arr.append(nums[i])
                    used[i] = True
                    backtrack(arr, used)
                    arr.pop()
                    used[i] = False
    
        backtrack([], [False] * len(nums))
        return res