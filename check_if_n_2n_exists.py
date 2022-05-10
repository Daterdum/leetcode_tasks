# https://leetcode.com/problems/check-if-n-and-its-double-exist/
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashed_vals = set()

        for num in arr:
            if hashed_vals & {2 * num, num / 2}:
                return True

            hashed_vals.add(num)
