class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
            
            for n in nums:
                if n in cur:
                    continue
                cur.append(n)
                backtrack(cur)
                cur.pop()
        backtrack([])
        return res