class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        lo, hi = 0, len(nums) - 1
        last = nums[-1]

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > last:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]