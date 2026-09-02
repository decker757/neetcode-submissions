class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while st and t > st[-1][1]:
                stIdx, temp = st.pop()
                res[stIdx] = i - stIdx
            st.append((i, t))
        
        return res
