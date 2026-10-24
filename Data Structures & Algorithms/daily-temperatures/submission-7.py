class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] #(temp, index)

        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                _, idx = st.pop()
                res[idx] = i - idx
            st.append((temp, i))
        
        return res