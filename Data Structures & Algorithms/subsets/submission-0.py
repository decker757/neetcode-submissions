class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            res.append(arr[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    return
                arr.append(nums[j])
                dfs(j + 1, arr)
                arr.pop()
        
        dfs(0, [])
        return res