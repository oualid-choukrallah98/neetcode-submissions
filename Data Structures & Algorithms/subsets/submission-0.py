class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset = []
        result = []
        self.helper(0, curset, result, nums)
        return result 
    def helper(self, i, curset, result, nums): 
        if i == len(nums): 
            result.append(curset.copy())
            return
        curset.append(nums[i])

        self.helper(i+1, curset, result, nums)
        curset.pop()

        self.helper(i+1, curset, result, nums)
        