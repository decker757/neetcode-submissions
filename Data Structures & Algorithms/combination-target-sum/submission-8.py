class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, arr, total):
            if total == target:
                res.append(arr.copy())
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                
                arr.append(nums[j])
                dfs(j, arr, total + nums[j])
                arr.pop()
        
        dfs(0, [], 0)

        return res