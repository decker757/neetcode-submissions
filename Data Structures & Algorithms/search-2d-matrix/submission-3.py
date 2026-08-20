class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                lo, hi = 0, COLS - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                
                return False
        return False


