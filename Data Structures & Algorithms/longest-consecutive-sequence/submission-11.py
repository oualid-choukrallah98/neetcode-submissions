class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        l = 0
        r = 1
        result = 1
        longest = 1
        while r < len(nums): 
            if nums[l] == nums[r]: 
                r += 1
                l += 1
            elif nums[l] +1 == nums[r]: 
                longest += 1
                result = max(result, longest)
                l += 1
                r += 1
            
            else : 
                longest = 1 
                l += 1
                r += 1
        
        return result 





     


