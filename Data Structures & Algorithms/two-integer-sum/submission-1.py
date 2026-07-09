class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] + nums[j] == target and i != j :
                    L.extend([i,j])
                    return L
         
        
    






        
        