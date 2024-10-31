n = int(input())
a = 0
arr = list(map(int, input().split()))
for x in arr:
    a += x
    print(a, end=" ")