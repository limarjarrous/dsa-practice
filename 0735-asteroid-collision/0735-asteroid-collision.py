class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                if stack and stack[-1] == -a:
                    stack.pop()
                    destroyed = True
                elif stack and stack[-1] > -a:
                    continue
                else:
                    stack.append(a)
        return stack