class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
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
        """
        n = len(s)
        memo = {}

        def backtrack(index):
            if index == n:
                return True
            if index in memo:
                return memo[index]

            for word in wordDict:
                if s.startswith(word, index):
                    next_start = index + len(word)
                    if backtrack(next_start):
                        memo[index] = True
                        return True

            memo[index] = False
            return False

        return backtrack(0)
