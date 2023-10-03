class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        turn_A, turn_B = 0, 0
        max_consecutive_A, max_consecutive_B = 0, 0

        for color in colors:
            if color == 'A':
                max_consecutive_A += 1
                max_consecutive_B = 0
                if max_consecutive_A >= 3:
                    turn_A += 1
            elif color == 'B':
                max_consecutive_B += 1
                max_consecutive_A = 0
                if max_consecutive_B >= 3:
                    turn_B += 1

        return turn_A > turn_B

