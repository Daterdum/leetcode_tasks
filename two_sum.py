from typing import List


class HashMap_1:
    """HashMap for list
    support for multiple elements on one key
    and element removal on get
    """

    def __init__(self, lst):
        for i, val in enumerate(lst):
            if self._dict.get(val):
                self._dict[val].append(i)
            else:
                self._dict[val] = [i]

    def __getitem__(self, val):
        if not self._dict.get(val):
            raise IndexError

        return self._dict[val].pop(0)


class HashMap:
    """HashMap for list
    support for multiple elements on one key
    and element removal on get
    """
    _data = {}

    def __init__(self, lst):
        for i, val in enumerate(lst):
            if self._data.get(val):
                self._data[val].append(i)
            else:
                self._data[val] = [i]

    def __getitem__(self, val):
        if not self._data.get(val):
            raise IndexError

        return self._data[val].pop(0)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = HashMap(nums)
        sorted_nums = sorted(nums)
        for index, num in enumerate(sorted_nums):
            if target - num >= 0:
                for second_index, second_num in enumerate(sorted_nums[index:]):
                    if num + second_num == target:
                        return [hash_map[num], hash_map[second_num]]

            else:
                for second_num in sorted_nums[index::-1]:
                    if num + second_num == target:
                        return [hash_map[num], hash_map[second_num]]
