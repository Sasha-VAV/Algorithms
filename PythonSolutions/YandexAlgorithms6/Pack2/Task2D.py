"""# FIXME
import time

start = time.time()
f = open("input.txt", "r")
s = f.readlines()
n, k = map(int, s[0].split())
arr = list(map(int, s[1].split()))
arr.sort()

def find_pos(x, arr):
    a = 0
    b = len(arr) - 1
    if b < a:
        return -1
    if x == arr[a]:
        return a
    if x > arr[b]:
        return b
    if x < arr[a]:
        return -1
    while b - a > 1:
        c = int((a + b) / 2)
        if arr[c] == x:
            return c
        elif arr[c] < x:
            a = c
        else:
            b = c
    return a if arr[a] <= x else -1


days = []
i_days = []
for x in arr:
    index = find_pos(x - k - 1, days)
    if index != -1 and x - days[index] > k:
        if i_days[index] == 1:
            y = days[index]
            days.pop(index)
            i_days.pop(index)
        else:
            i_days[index] -= 1
        if len(days) > 0 and days[-1] < x:
            days.append(x)
            i_days.append(1)
        else:
            index = find_pos(x, days)
            days.insert(index + 1, x)
            i_days.insert(index + 1, 1)
    elif index != -1 and x - days[index] == k:
        i_days[index] += 1
    elif len(days) > 0 and x - days[0] == 0:
        i_days[0] += 1
    else:
        if len(days) > 0 and days[-1] < x:
            days.append(x)
            i_days.append(1)
        else:
            index = find_pos(x, days)
            days.insert(index + 1, x)
            i_days.insert(index + 1, 1)
    

print(sum(i_days))


'''def find_pos(x, arr):
    a = 0
    b = len(arr) - 1
    while a < b:
        c = int((a + b + 1) / 2)
        if arr[c] > x:
            if c > 0 and arr[c-1] <= x:
                return c
            elif c == 0:
                return 0
            else:
                b = c
        else:
            a = c
    return -1


m = 0
i = 0
#for i in range(7, len(arr)):
#    if arr[i] - arr[i - 7] <= 2:
#        print(i, arr[i-9:i + 2])
i = 0
while i != -1:
    #print(i, arr[i])
    index = find_pos(arr[i] + k, arr)
    if index == -1 or index == i:
        m = max(m, len(arr) - i)
        break
    m = max(m, index - i)
    #if m == 6: print(i)

    i = index

print(m)'''
print(time.time() - start)

#FIXME DOES NOT WORK!!!"""


print("WATCH JAVA SOLUTIONS!!!")