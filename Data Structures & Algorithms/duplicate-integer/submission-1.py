class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums : 
            hashset.add(number)

        if len(hashset)!= len(nums):
            return True
        else : 
            return False

            