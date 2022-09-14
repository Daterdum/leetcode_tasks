class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for ind, num in enumerate(nums):
            other_ind = map_.get(target - num)
            if other_ind is not None:
                return [ind, other_ind]

            map_[num] = ind
