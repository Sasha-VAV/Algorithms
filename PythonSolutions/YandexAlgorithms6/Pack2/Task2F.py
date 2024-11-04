n = int(input())
arr = list(map(int, input().split()))

res = 0
curr = 0
args = 0
for i in range(n - 2):
    args += arr[-(i + 1)]
    curr += arr[-(i + 2)] * args
    res += curr * arr[-(i + 3)]
    res %= 10**9 + 7

print(res)
