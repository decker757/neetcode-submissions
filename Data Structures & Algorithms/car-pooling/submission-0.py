class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        
        for passengers, start, end in trips:
            points.append((start, passengers))
            points.append((end, -passengers))
        points.sort()

        totalPassengers = 0
        for point, passengers in points:
            if totalPassengers > capacity:
                return False
            totalPassengers += passengers
        
        return True