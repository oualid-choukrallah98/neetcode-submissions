class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            hashset.add(num)
            
        return len(nums) != len(hashset)


        