class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range (0,len(nums)):
            if i > 0 and  nums[i] == nums[i-1]:
                continue 
            L = i + 1
            R = len(nums) - 1 
            while L < R :
                if nums[i] + nums[L] + nums[R] < 0 :
                    L += 1
                elif nums[i] + nums[L] + nums[R] > 0 :
                    R -= 1
                else : 
                    res.append([nums[i],nums[R],nums[L]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R :
                        L += 1
        return res
                        
                        

                

        