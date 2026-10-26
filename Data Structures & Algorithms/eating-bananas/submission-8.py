class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = float('inf')
        l, r = 1, max(piles)
        
        while l <= r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            
            if time <= h:
                r = k - 1
                minSpeed = min(minSpeed, k)
            else:
                l = k + 1

        return minSpeed

