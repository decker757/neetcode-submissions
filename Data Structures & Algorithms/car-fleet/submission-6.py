class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_ls = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd
            if not time_ls or time > time_ls[-1]:
                time_ls.append(time)
        return len(time_ls)


            
        
