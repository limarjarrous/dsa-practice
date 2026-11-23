class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        
        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
        return [[a, b, c] for a, b, c in result]
        