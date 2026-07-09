class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [1] * len(nums)
        left_product = [1] * len(nums)
        for i in range (len(nums)):
            j = i +1
            while j < len(nums) :
                right_product[i] *= nums[j]
                j = j + 1
        for i in range(len(nums)) : 
            j = i - 1
            while j >= 0:
                left_product[i] *= nums[j]
                j = j - 1
        return [x * y for x, y in zip(right_product,left_product)]

        
        