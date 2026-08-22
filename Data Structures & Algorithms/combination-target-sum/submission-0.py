class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb, curcomb = [], []
        self.helper(0, target, comb, curcomb, nums)
        return comb 
    
    def helper(self, i, target, comb, curcomb, nums): 
        
        if sum(curcomb) == target: 
            comb.append(curcomb.copy())
            return 
        if i >= len(nums) or sum(curcomb) > target: 
            return 
        
        curcomb.append(nums[i])
        self.helper(i, target, comb, curcomb, nums)

        curcomb.pop()
        self.helper(i+1, target, comb, curcomb, nums)


