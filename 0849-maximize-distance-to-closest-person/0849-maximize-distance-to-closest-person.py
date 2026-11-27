class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        last_one = -1
        max_dist = 0
        best_seat = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                # case 1: leading zeros
                if last_one == -1:
                    if i > max_dist:
                        max_dist = i
                        best_seat = 0
                
                # case 2: middle zeros
                else:
                    dist = (i - last_one) // 2
                    if dist >  max_dist:
                        max_dist = dist
                        best_seat = last_one + dist

                last_one = i
        
        if seats[-1] == 0:
            dist = (n - 1) - last_one
            if dist > max_dist:
                    max_dist = dist
                    best_seat = n - 1

        return max_dist