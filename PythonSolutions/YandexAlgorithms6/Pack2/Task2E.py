'''#import time


#start = time.time()
f = open("input.txt", "r")
s = f.readlines()
n = int(s[0])
arr = list(map(int, s[1].split()))
arr.sort()
answer = ""
a = len(arr)
if a % 2 == 1:
    answer += str(arr[a//2]) + " "
    a = a // 2 - 1
    b = a + 2
else:
    a = a // 2 - 1
    b = a + 1

left = arr[:a + 1]
right = arr[b:]

while len(right) > 0:
    answer += str(left[-1]) + " " + str(right[0]) + " "
    left.pop(-1)
    right.pop(0)


print(answer)
#print(time.time() - start)'''

print("WATCH JAVA SOLUTIONS")