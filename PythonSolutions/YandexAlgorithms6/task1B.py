a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = a + 1
n = c + 1
if m + n > b + 1 + d + 1:
    m = b + 1
    n = d + 1
if m + n > max(c, d) + 2:
    m = 1
    n = max(c, d) + 1
if m + n > max(a, b) + 2:
    m = max(a, b) + 1
    n = 1
if a + c == 0 or b + d == 0:
    m = 1
    n = 1
if a == 0:
    m = 1
    n = c + 1
if b == 0:
    m = 1
    n = d + 1
if c == 0:
    m = a + 1
    n = 1
if d == 0:
    m = b + 1
    n = 1

print(m, n)
