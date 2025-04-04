from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        references = []
        for word in strs:
            count = Counter(word)
            for i, reference in enumerate(references):
                if reference == count:
                    ans[i].append(word)
                    break
            else:
                ans.append([word])
                references.append(count)
        return ans


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
