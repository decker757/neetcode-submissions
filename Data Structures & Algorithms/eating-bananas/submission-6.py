class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 10000000
        lo, hi = 1, max(piles)

        while lo <= hi:
            spd = (lo + hi) // 2
            time = 0

            for p in piles:
                time += math.ceil(p/spd)
            if time <= h:
                res = spd
                hi = spd - 1
            else:
                lo = spd + 1
        return res