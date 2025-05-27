class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        global_sum = (1 + n) * n // 2
        m_sum = n // m
        m_sum = m_sum * m * (m_sum + 1) // 2
        return global_sum - 2 * m_sum