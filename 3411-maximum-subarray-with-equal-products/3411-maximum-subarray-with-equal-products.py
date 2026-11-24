class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1
        max_prod = prod(nums)

        for i in range(n):
            curr_prod = curr_gcd = curr_lcm = nums[i]
            
            for j in range(i + 1, n):
                curr_prod *= nums[j]
                if curr_prod > max_prod:
                    break

                curr_gcd = gcd(curr_gcd, nums[j])
                curr_lcm = lcm(curr_lcm, nums[j])

                if curr_prod == curr_gcd * curr_lcm:
                    max_len = max(max_len, j - i + 1)
        
        return max_len