class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1

        while a + b + c < n:
            a, b, c = b, c, b + c

        return True if a + b + c == n else False
