class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        max_freq = 0
        max_len = 0

        left = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]
            
            curr_len = right - left + 1
            while curr_len - max_freq > k:
                freq[s[left]] -= 1
                curr_len -= 1
                left += 1
            
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len