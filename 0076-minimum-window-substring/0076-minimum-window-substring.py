class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""
         
        t_freq = Counter(t)
        missing = len(t)
        best_len = float('inf')
        best_start = 0
        left = 0

        for right, char in enumerate(s):
            if char in t_freq:
                if t_freq[char] > 0:
                    missing -= 1
                t_freq[char] -= 1

            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                if s[left] in t_freq:
                    t_freq[s[left]] += 1
                    if t_freq[s[left]] > 0:
                        missing += 1
                
                left += 1
                
        return "" if best_len == float('inf') else s[best_start : best_start + best_len]
