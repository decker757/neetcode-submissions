class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1]
            val = 1
            for j in range(1, i + 1):
                val = val * (i - j + 1) // j
                row.append(val)
            res.append(row)
        return res