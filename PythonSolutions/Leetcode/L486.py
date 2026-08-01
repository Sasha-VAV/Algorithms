class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(p1_score, p2_score, l_boundary, r_boundary, p1_turn):
            if l_boundary > r_boundary:
                return p1_score >= p2_score

            left = nums[l_boundary]
            right = nums[r_boundary]

            if p1_turn:
                return dfs(p1_score + left, p2_score, l_boundary + 1, r_boundary, False) or dfs(p1_score + right,
                                                                                                p2_score, l_boundary,
                                                                                                r_boundary - 1, False)
            return dfs(p1_score, p2_score + left, l_boundary + 1, r_boundary, True) and dfs(p1_score, p2_score + right,
                                                                                            l_boundary, r_boundary - 1,
                                                                                            True)

        return dfs(0, 0, 0, len(nums) - 1, True)
