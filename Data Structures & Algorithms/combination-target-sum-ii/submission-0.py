class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        comb, curcomb = [], []
        self.helper(0, curcomb, comb, target, candidates, 0)
        return comb
    
    def helper(self, i, curcomb, comb, target, nums, total): 
        if total == target :
            comb.append(curcomb.copy())
            return
        if i >=len(nums) or total > target:
            return 
        
        curcomb.append(nums[i])

        self.helper(i+1, curcomb, comb, target, nums, total + nums[i])
        curcomb.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1, curcomb, comb, target, nums, total)


