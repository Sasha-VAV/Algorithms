def bin_search(x, arr):
    if len(arr) == 0:
        return -1
    if x > arr[0]:
        return 0
    if x <= arr[-1]:
        return -1
    a = 0
    b = len(arr) - 1
    while b - a > 1:
        c = (a + b) // 2
        if arr[c] >= x:
            a = c
        elif arr[c] < x:
            b = c
    return b


f = open("input.txt", "r")
s = f.readlines()
n = int(s[0])
arr = list(map(int, s[1].split()))
v = []
v_i = []
for i in range(len(arr) - 1, -1, -1):
    x = arr[i]
    y = bin_search(x, v)
    arr[i] = v_i[y] if y > -1 else -1
    if len(v) > 0 and x > v[0]:
        v.insert(0, x)
        v_i.insert(0, i)
    elif len(v) > 0 and x == v[0]:
        v_i[0] = i
    else:
        if y > -1:
            v = v[y:]
            v_i = v_i[y:]
            v.insert(0, x)
            v_i.insert(0, i)
        else:
            v = [x]
            v_i = [i]

print(*arr)