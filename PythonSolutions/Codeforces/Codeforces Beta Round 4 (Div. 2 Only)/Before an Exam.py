d, sum_time = map(int, input().split())
min_time, max_time = 0, 0
possible_times = dict()
for i in range(d):
    a, b = map(int, input().split())
    min_time += a
    max_time += b
    tmp = possible_times
    possible_times.clear()
    pass
print("YES" if min_time <= sum_time <= max_time else "NO")