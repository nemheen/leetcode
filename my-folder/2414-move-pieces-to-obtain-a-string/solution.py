class Solution:
    def canChange(self, start: str, target: str) -> bool:

        start_positions = [(c, i) for i, c in enumerate(start) if c in "LR"]
        target_positions = [(c, i) for i, c in enumerate(target) if c in "LR"]

        if len(start_positions) != len(target_positions):
            return False

        for (ch1, p1), (ch2, p2) in zip(start_positions, target_positions):
            if ch1 != ch2:
                return False
            if ch1 == 'L' and p1 < p2:
                return False
            if ch1 == 'R' and p1 > p2:
                return False
                


        return True
        
