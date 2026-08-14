class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums) - 1
        while L <= R : 
            mid = (L+R) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[L]: 
                if target > nums[R] or target < nums[mid]: 
                    R = mid - 1 
                else : 
                    L = mid + 1
            else : 
                if target < nums[L] or target  > nums[mid] : 
                    L = mid + 1
                else : 
                    R = mid - 1 
        return - 1                

        