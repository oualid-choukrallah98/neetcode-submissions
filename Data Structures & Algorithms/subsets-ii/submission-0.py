class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cursub, sub = [], []

        def helper(i, cursub, sub, nums): 
            if i ==len(nums): 
                sub.append(cursub.copy())      
                return 

            cursub.append(nums[i])

            helper(i+1, cursub, sub, nums)
            cursub.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]: 
                i += 1
            helper(i+1, cursub, sub, nums)

        helper(0,cursub, sub, nums)
        return sub
