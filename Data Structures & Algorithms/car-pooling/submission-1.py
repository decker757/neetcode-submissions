class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # num_passengers, from, to
        points = []
        total_passengers = 0

        for passengers, start, end in trips:
            points.append((start, passengers))
            points.append((end, -passengers))
        points.sort()

        for start, passengers in points:
            if total_passengers > capacity:
                return False
            total_passengers += passengers
        
        return True