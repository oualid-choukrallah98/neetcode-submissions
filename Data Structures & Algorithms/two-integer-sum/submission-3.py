class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for indice, num in enumerate (nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], indice]
            hash_map[num]=indice 
        
       
        
         
        
    






        
        