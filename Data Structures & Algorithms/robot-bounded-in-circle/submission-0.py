class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        origin = [0, 0]
        cur_direction = [0, 1]
        cur_pos = [0, 0]

        for i in instructions:
            if i == "G":
                cur_pos[0] += cur_direction[0]
                cur_pos[1] += cur_direction[1]
            elif i == "L":
                cur_direction[0], cur_direction[1] = -cur_direction[1], cur_direction[0]
            elif i == "R":
                cur_direction[0], cur_direction[1] = cur_direction[1], -cur_direction[0]

        return cur_pos == origin or cur_direction != [0, 1]