class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        right_streak = 1
        left_streak = 1
        #left multiplication
        for i in range(1,len(nums)):
            left_streak *= nums[i-1]
            result[i] = left_streak

        #right multiplication
        for i in range(len(nums)-2,-1,-1):
            right_streak *= nums[i+1]
            result[i] *= right_streak
            

        return result




        