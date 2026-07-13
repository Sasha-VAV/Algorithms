PRECOMPUTED_INTEGERS = []

for number_len in range(2, 10):
    curr = 0
    delta_integer = 0
    for i in range(1, number_len + 1):
        curr *= 10
        curr += i
        delta_integer *= 10
        delta_integer += 1
    
    for _ in range(10 - number_len):
        PRECOMPUTED_INTEGERS.append(curr)
        curr += delta_integer


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        left = bisect.bisect_left(PRECOMPUTED_INTEGERS, low)
        right = bisect.bisect_right(PRECOMPUTED_INTEGERS, high)
        return PRECOMPUTED_INTEGERS[left:right]