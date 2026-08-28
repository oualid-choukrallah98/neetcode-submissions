class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        def dfs(start,end):
            memo = {}
            def helper(i): 
                if i in memo: 
                    return memo[i]

                if i >= end: 
                    return 0 
                
                previousrob = helper(i+1)
                currentrob = nums[i] + helper(i+2)
                memo[i] = max(previousrob, currentrob)

                return memo[i]
            return helper(start)
        
        return max(dfs(0,len(nums)-1), dfs(1,len(nums)))

        