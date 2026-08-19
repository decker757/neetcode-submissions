class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pairs = sorted(zip(position, speed), reverse=True)

        for p, s in pairs:
            st.append((target - p) / s)
            
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        return len(st)
        

        