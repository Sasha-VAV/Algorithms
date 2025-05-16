from typing import List
import heapq


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = []
        for word, group in zip(words, groups):
            tmp = dp.copy()
            max_arr = []
            while tmp:
                _, group2, word_arr = heapq.heappop(tmp)
                word2 = word_arr[-1]
                if len(word2) != len(word) or group == group2: continue
                diff = 0
                for c1, c2 in zip(word, word2):
                    if c1 != c2: diff += 1
                    if diff > 1: break
                if diff != 1: continue
                max_arr = word_arr
                break
            heapq.heappush(dp, (-len(max_arr) - 1, group, max_arr + [word]))
        return heapq.heappop(dp)[2]



if __name__ == '__main__':
    words = ["a","b","c","d"]
    groups = [1,2,3,4]
    print(Solution().getWordsInLongestSubsequence(words, groups))