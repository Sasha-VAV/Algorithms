class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        :param path: unix path to normalize
        :return: normalized path
        """
        if not path: return "."
        abs_path = path[0] == "/"
        path = path.split("/")
        stack = deque()
        for p in path:
            if not p: continue
            if p == ".": continue
            if p == "..":
                if stack and stack[-1] != "..":
                    stack.pop()
                    continue
                if abs_path:
                    continue
            stack.append(p)
        if not stack: return "/" if abs_path else "."
        res = "/" if abs_path else ""
        res += "/".join(stack)
        return res