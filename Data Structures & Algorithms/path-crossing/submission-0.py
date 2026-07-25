class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [(0, 0)]
        x, y, = 0, 0
        for p in path:
            if p == "N":
                y += 1
                pos.append((x, y))
            elif p == "E":
                x += 1
                pos.append((x, y))
            elif p == "W":
                x -= 1
                pos.append((x, y))
            else:
                y -= 1
                pos.append((x, y))
        
        unique_pos = set(pos)

        return len(unique_pos) != len(pos)