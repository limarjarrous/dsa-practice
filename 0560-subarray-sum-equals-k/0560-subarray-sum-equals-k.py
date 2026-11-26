class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            remaining = current_sum - k

            if remaining in freq:
                total_subarrays += freq[remaining]
                
            freq[current_sum] = freq.get(current_sum, 0) + 1
            
        return total_subarrays
