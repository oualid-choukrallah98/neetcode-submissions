class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in nums: 
            if (num -1) not in numset :
                lenght = 0
                while (num + lenght) in numset : 
                    lenght += 1
                longest = max(longest,lenght)
        return longest 
                    

        