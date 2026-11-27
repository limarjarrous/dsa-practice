class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        completed = {}
        day = 0
        for i in range(len(tasks)):
            if tasks[i] not in completed:
                completed[tasks[i]] = day
                day += 1
            else:
                if day <= completed[tasks[i]] + space:
                    day = completed[tasks[i]] + space + 1
                completed[tasks[i]] = day
                day += 1
        
        return day
