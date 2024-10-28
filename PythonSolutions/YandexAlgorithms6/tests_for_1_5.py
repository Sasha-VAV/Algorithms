f = open("task1E_test_case_descriptions.txt", "r")
s = f.readlines()
f.close()
del f
f = open("task1E.txt", "w")
f.write(s[0])
for i in s[1:]:
    f.write(i[:i.find(":") - 1] + "\n")
