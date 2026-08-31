class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums: 
            lenght = 1
            if num -1 not in numset: 
                while num + lenght in numset: 
                    lenght += 1
                
            
            res = max(res, lenght)
        
        return res 







