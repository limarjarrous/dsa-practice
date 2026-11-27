class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        completed = {}
        day = 0
        for task in tasks:
            day += 1
            if task in completed:
                if day <= completed[task] + space:
                    day = completed[task] + space + 1
            completed[task] = day
        return day