s = input()
a, b = map(int, s[:s.rfind(" ")].split())
s = s[s.rfind(" ") + 1:]
if s == "freeze":
    print(min(a, b))
elif s == "heat":
    print(max(a, b))
elif s == "auto":
    print(b)
elif s == "fan":
    print(a)