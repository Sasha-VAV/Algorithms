class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        seen = set()
        stack = deque()

        for c in s:
            counter[c] -= 1
            if c in seen: continue

            while stack and stack[-1] > c and counter[stack[-1]]:
                seen.remove(stack.pop())
            
            seen.add(c)
            stack.append(c)
        return "".join(stack)