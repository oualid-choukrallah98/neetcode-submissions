class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums : 
            if num not in dict_num:
                dict_num[num] = 1
            else :
                return True
        return False

        
    
        