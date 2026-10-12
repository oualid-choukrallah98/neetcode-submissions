class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums 
        self.k = k 
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]

        

#3
#[1, 2, 3, 3, 3, 3, 5, 6, 7]