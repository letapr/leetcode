class Solution:
    """
    solution must be O(n)
    solution: iterate, if nums[i] is >= target, return i
    """
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
if __name__ == "__main__":
    print(0)