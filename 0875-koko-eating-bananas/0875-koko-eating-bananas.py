class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def get_hours(k):
            hours = 0
            for p in piles:
                if p <= k:
                    hours += 1
                else:
                    hours += p // k
                    hours += 1 if p % k else 0
            return hours


        left = 1
        right = max(piles)
        bananas_per_hour = max(piles)
        while left <= right:
            mid = (right + left) // 2
            required_hours = get_hours(mid)
            
            if required_hours <= h:
                bananas_per_hour = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return bananas_per_hour