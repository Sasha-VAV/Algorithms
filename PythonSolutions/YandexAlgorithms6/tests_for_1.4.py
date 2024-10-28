import subprocess



f = open("task1D.txt", "r")
s = f.readlines()
n = int(s[0])
for i in range(1,n+1):
    temp = s[i]
    process = subprocess.Popen(
        ['python', 'task1D.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    ans, error = process.communicate(input = temp)
    print(ans.strip())