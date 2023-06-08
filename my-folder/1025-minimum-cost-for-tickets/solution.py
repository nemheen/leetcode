class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        day_7, day_30 = 0, 0
        f = [0] * n
        f[0] = min(costs)
        for i in range(1, n):
            while days[day_7] + 6 < days[i]:
                day_7 += 1
            while days[day_30] + 29 < days[i]:
                day_30 += 1
            option1 = costs[0] + f[i - 1]
            option2 = costs[1] + (f[day_7 - 1] if day_7 >= 1 else 0)
            option3 = costs[2] + (f[day_30 - 1] if day_30 >= 1 else 0)
            f[i] = min(option1, option2, option3)
        return f[n - 1]
