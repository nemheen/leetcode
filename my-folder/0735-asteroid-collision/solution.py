class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                top = stack.pop()

                if abs(top) == abs(asteroid):
                    # Both asteroids explode
                    #nothing to do
                    break
                elif abs(top) > abs(asteroid):
                    # Only the current asteroid explodes
                    stack.append(top)
                    break
            else:
                # No collision, push back
                stack.append(asteroid)

        return stack

