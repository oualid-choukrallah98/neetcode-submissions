class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        for i in range(len(nums)):
            if min_value > nums[i]:
                min_value =  nums[i]
        return min_value

        