class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def helper(nums, k):
            curr_sum = 0
            seen_at = {0: -1}
            longest = 0

            for idx, num in enumerate(nums):
                curr_sum += num
                mod = curr_sum % k

                if mod in seen_at:
                    longest = max(longest, idx - seen_at[mod])
                else:
                    seen_at[mod] = idx

            return longest
        

        ans = helper(nums, k)
        for i in range(len(nums)):
            nums[i] = -nums[i]
            ans = max(ans, helper(nums, k))
            nums[i] = -nums[i]
        return ans