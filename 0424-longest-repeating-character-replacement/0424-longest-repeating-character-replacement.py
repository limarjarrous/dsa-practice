class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        max_freq = 0
        max_len = 0

        left = 0

        for right, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            
            max_freq = max(max_freq, freq[char])
            
            curr_len = right - left + 1
            while curr_len - max_freq > k:
                freq[s[left]] -= 1
                curr_len -= 1
                left += 1
            
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len