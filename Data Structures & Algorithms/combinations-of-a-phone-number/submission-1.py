class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, letters):
            if i >= len(digits):
                res.append(letters)
                return
            
            for ch in numToChars[digits[i]]:
                backtrack(i + 1, letters + ch)

        if digits:
            backtrack(0, "")

        return res

