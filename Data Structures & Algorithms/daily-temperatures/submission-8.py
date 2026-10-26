class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for idx, tmp in enumerate(temperatures):
            while st and tmp > st[-1][0]:
                _, index = st.pop()
                res[index] = idx - index
            st.append((tmp, idx))

        return res