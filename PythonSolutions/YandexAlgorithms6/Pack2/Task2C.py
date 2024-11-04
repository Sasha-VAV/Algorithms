f = open("input.txt", "r")
s = f.readlines()
n, r = map(int, s[0].split())
left = 0
k = 0
arr = list(map(int, s[1].split()))
for i in range(1, n):
    while arr[i] - arr[left] > r:
        k += n - i
        left += 1

print(k)
