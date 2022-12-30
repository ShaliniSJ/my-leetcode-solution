class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        for i,vals in enumerate (nums):
            diff =target - vals
            if diff in hash:
                return [hash[diff],i]
            hash[vals] = i
