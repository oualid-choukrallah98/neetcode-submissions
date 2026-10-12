class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb, curr_comb = [], []
        self.helper(0, comb, curr_comb, target, nums)
        return comb

    def helper(self, i, comb, curr_comb, target, nums): 
        if sum(curr_comb) == target: 
            comb.append(curr_comb.copy())
            return
        if i >= len(nums) or sum(curr_comb) > target: 
            return 

        curr_comb.append(nums[i])
        self.helper(i, comb, curr_comb, target, nums)

        curr_comb.pop()
        self.helper(i+1, comb, curr_comb, target, nums)
        
        
        
        