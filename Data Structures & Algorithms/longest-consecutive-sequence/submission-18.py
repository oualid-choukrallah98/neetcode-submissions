class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        numset = set(nums)
        for num in nums: 
            if num - 1 not in numset: 
                lenght = 1
                while num + lenght in numset: 
                    lenght += 1
            
                res = max(res, lenght)
        
        return res
            




        