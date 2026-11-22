class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        visited = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            
            visited[num] = i

        return []