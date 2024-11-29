f = open("input.txt", "w")

a = 2 * (10**5)
s = str(a) + "\n"
for i in range(a, -1, -1):
    s += str(i) + " "

f.write(s)