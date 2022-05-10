# https://leetcode.com/problems/duplicate-zeros/
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        for elem in arr:
            if elem == 0:
                zero_count += 1

