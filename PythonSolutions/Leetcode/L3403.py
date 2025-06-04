class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        s = ""
        n = len(word) - numFriends + 1
        for i in range(len(word)):
            s = max(s, word[i:i+n])
        return s
