class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hash_num:
                return [hash_num[diff], index]
            hash_num[value] = index
        
            
        
        
        