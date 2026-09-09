class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, arr, total):
            if total == target:
                res.append(arr[:])

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    return
                
                arr.append(candidates[j])
                backtrack(j + 1, arr, total + candidates[j])
                arr.pop()
            
        backtrack(0, [], 0)

        return res