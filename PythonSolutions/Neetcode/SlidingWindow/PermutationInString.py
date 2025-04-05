class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 52
        count2 = [0] * 52
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i, c in enumerate(s2[len(s1):]):
            prev = s2[i]
            count2[ord(prev) - ord('a')] -= 1
            count2[ord(c) - ord('a')] += 1
            if count1 == count2:
                return True
        return False


if __name__ == '__main__':
    s1 = "a"
    s2 = "ab"
    print(Solution().checkInclusion(s1, s2))
