class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i, tmp in enumerate(temperatures):
            while st and tmp > st[-1][0]:
                t, index = st.pop()
                res[index] = (i - index)
            st.append((tmp, i))
        return res
