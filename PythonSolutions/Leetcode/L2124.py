class Solution:
    def checkString(self, s: str) -> bool:
        stage = 0 # 0 - expecting a or b 1 - only b
        for c in s:
            if c == "a" and stage == 1:
                return False
            if c == "b":
                stage = 1
        return True