class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        result = 1
        hashset = set()
        for num in nums: 
            hashset.add(num)
        
        for num in nums:
            if num - 1 not in hashset: 
                sequence = 1  
                i = 1
                while num + i in hashset:
                    sequence += 1
                    i += 1
                result = max(result, sequence) 
            
        return result



        