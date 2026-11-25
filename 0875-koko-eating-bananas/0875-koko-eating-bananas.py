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


        min_speed = 1
        max_speed = max(piles)

        while min_speed <= max_speed:
            speed = (max_speed + min_speed) // 2
            required_hours = get_hours(speed)
            
            if required_hours <= h:
                max_speed = speed - 1
            else:
                min_speed = speed + 1
        
        return min_speed