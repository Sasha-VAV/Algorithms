import numpy as np

"""Task 9 from LeetCode
Made for the best speed, without converting input integer value to string
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = 10
        while a <= x:
            a *= 10
        x += a
        a //= 10
        while x > 99:
            if x % 10 != x % (a * 10) // a:
                return False
            x //= 10
            a //= 10
            x %= a
            x += a
            a //= 10
        return True


results = np.array([[25, 99.98], [16.84, 13.22]])
sol = Solution()
print("Hello, this program solves task 9 from LeetCode")
print(f"Runtime {results[0][0]}ms, beats {results[0][1]}% 👍")
print(f"Memory {results[1][0]}MB, beats {results[1][1]}% 😔")
print(f'Exit value "stop"')
while True:
    s = input("Enter your value: ")
    if s == "stop":
        break
    a = int(s)
    if sol.isPalindrome(a):
        print(f"{a} is a palindrome")
    else:
        print(f"{a} is not a palindrome")