f = open("input.txt", "w")
f.write("150000 10000\n")
s = ""
for i in range(150000):
    s += str(i) + " "
f.write(s)