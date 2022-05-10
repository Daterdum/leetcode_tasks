import random


class Solution:
    def mySqrt(self, x: int) -> int:
        a = 1
        while a * a <= x:
            a += 1

        return a - 1
