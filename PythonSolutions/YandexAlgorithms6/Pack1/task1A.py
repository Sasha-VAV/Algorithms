x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = int(input())
b = int(input())

s = ""
if b >= y2:
    s += "N"
elif b <= y1:
    s += "S"

if a <= x1:
    s += "W"
elif a > x2:
    s += "E"

print(s)
