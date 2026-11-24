class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        
        @cache
        def can_split(start):
            if start == n:
                return True
            
            for j in range(start + 1, n + 1):
                if s[start:j] in wordDict and can_split(j):
                    return True
            
            return False

        return can_split(0)
