class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        lower_bound, higher_bound = 0, ROWS - 1

        while lower_bound <= higher_bound:
            mid_bound = (lower_bound + higher_bound) // 2
            if matrix[mid_bound][0] <= target <= matrix[mid_bound][-1]:
                l, r = 0, COLS - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid_bound][m] == target:
                        return True
                    elif matrix[mid_bound][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False
            elif matrix[mid_bound][0] > target:
                higher_bound = mid_bound - 1
            else:
                lower_bound = mid_bound + 1
        return False

