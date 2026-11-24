class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r, k):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if k == 0:
                        return False
                    return is_palindrome(l + 1, r, k - 1) or is_palindrome(l, r - 1, k - 1)
            return True
        
        return is_palindrome(0, len(s) - 1, 1)