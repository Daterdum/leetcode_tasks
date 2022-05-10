from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        len_ = len(arr)
        if len_ < 3:
            return False

        i = 1
        while arr[i] > arr[i - 1]:
            i += 1
            if i == len_:
                return False

        while i < len_:
            if i == 1:
                return False
            if arr[i] >= arr[i - 1]:
                return False
            i += 1

        return True
