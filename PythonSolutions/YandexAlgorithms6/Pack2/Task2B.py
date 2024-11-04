n, k = map(int, input().split())
left = 0
count = 0
inputs = list(map(int, input().split()))
arr = [inputs[0]]
for i in range(1, n + 1):
    x = inputs[i - 1]
    arr += [arr[i - 1] + x]
    if arr[i] - arr[left] == k:
        count += 1
    else:
        while arr[i] - arr[left] > k:
            left += 1
        if arr[i] - arr[left] == k:
            count += 1
print(count)
