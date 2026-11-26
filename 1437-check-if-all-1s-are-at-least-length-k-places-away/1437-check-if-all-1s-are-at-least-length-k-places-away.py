class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last = -1
        for idx, num in enumerate(nums):
            if num == 0:
                continue
            if last == -1:
                last = idx
            elif idx - last <= k:
                return False
            else:
                last = idx
        return True