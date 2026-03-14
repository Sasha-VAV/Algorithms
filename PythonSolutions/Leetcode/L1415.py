class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k -= 1
        curr = 1 << (n - 1)
        if k >= curr * 3: return ""
        c = k // curr
        match c:
            case 0:
                prefix = ["a"]
            case 1:
                prefix = ["b"]
            case 2:
                prefix = ["c"]
        k %= curr
        def select_next(character, shift):
            ref = "abc"
            match character:
                case "a": return ref[shift+1]
                case "b": return "a" if shift == 0 else "c"
                case "c": return ref[shift]

        while len(prefix) < n:
            curr >>= 1
            c = k // curr
            k %= curr
            prefix.append(select_next(prefix[-1], c))
        return "".join(prefix)