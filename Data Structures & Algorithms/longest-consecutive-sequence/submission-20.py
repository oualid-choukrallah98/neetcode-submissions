class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 0 
        for num in nums: 
            if num -1 in numset: 
                continue 
            longest = 1
            current = num 
            while current + 1 in numset: 
                current += 1
                longest += 1
            
            result = max(result, longest)
        return result 












