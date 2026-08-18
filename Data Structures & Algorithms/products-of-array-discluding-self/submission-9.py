class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        p1 = 1
        p2 = 1
        for i in range(len(nums)):
            res[i] = p1
            p1 *= nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            res[i] *= p2
            p2 *= nums[i]

        return res 

       