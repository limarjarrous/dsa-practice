class Solution:
    def checkString(self, s: str) -> bool:
        first_b = None
        last_a = None

        for i in range(len(s)):
            if first_b is None and s[i] == 'b':
                first_b = i
            if s[i] == 'a':
                last_a = i
        
        return True if last_a is None or first_b is None or last_a < first_b else False 
        