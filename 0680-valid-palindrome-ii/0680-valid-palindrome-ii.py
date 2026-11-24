class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def is_palindrome(l, r, k):
            if k > 1:
                return False
            if l >= r and k <= 1:
                return True
            
            if s[l] == s[r]:
                return is_palindrome(l + 1, r - 1, k)
            else:
                return is_palindrome(l + 1, r, k + 1) or is_palindrome(l, r - 1, k + 1) or is_palindrome(l + 1, r - 1, k + 2)
        
        return is_palindrome(0, len(s) - 1, 0)