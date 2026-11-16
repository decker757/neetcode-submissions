class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                if candidates[j] + total > target:
                    continue
                
                cur.append(candidates[j])
                backtrack(j + 1, cur, total + candidates[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return res