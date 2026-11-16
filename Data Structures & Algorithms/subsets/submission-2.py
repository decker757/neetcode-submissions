class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, cur):
            res.append(cur[:])
    
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cur.append(nums[j])
                backtrack(j + 1, cur)
                cur.pop()
        
        backtrack(0, [])

        return res