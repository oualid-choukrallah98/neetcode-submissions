class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.helper(0, nums)
    
    def helper(self, i, nums): 

        if i == len(nums): 
            return [[]]
        resperm = []
        perm = self.helper(i+1, nums)
        for p in perm: 
            for j in range(len(p)+1): 
                pcopy = p.copy()
                pcopy.insert(j, nums[i])
                resperm.append(pcopy)
        return resperm