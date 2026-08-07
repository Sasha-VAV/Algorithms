class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primes = [2, 3, 5, 7]
        counts = [0] * 4
        prev = None
        while t > 1:
            
            for i, prime in enumerate(primes):
                if t % prime == 0:
                    counts[i] += 1
                    t //= prime
            if t == prev and t > 1:
                return "-1"
            prev = t
        digit_counts = {}
        for x in range(0, 10):
            digits = [0] * 4
            number = str(x)
            while x > 1:
                for i, prime in enumerate(primes):
                    if x % prime == 0:
                        digits[i] += 1
                        x //= prime
                        break
            digit_counts[number] = digits
        
        num_counts = [0] * 4
        for c in num:
            for i, x in enumerate(digit_counts[c]):
                num_counts[i] += x
        
        demands = [max(0, counts[i] - num_counts[i]) for i in range(4)]

        if not any(demands):
            return num
        supply = [0] * 4
        numbers = []
        tmp_num = "1" * sum(demands) + num

        for i, c in enumerate(reversed(tmp_num)):
            for j, x in enumerate(digit_counts[c]):
                target = counts[j]
                supplier = num_counts[j]
                demands[j] += min(max(0, target - supplier + x), x)

            best_supplier = [0] * 4
            best_value = float('inf')
            best_negative_supply = -float('inf')
            for x in range(9, 1, -1):
                curr_value = sum(max(0, demands[j] - a - supply[j]) for j, a in enumerate(digit_counts[str(x)]))
                negative_supply = sum(min(0, max(demands[j] - supply[j], 0) - a) for j, a in enumerate(digit_counts[str(x)]))
                if curr_value < best_value or curr_value == best_value and negative_supply > best_negative_supply:
                    best_supplier = x
                    best_value = curr_value
                    best_negative_supply = negative_supply
            
            numbers.append(best_supplier)
            best_supplier = digit_counts[str(best_supplier)]

            for j in range(4):
                supply[j] += best_supplier[j]
            
            if best_value == 0:
                break

        # i = num of number to change to achieve out goals
        # may have bug, but i'll test with the submission
        # print(numbers)
        counter_numbers = [0] * 10
        for x in numbers:
            counter_numbers[x] += 1
            
        overflow = len(numbers) > len(num)
        new_numbers = []
        transform = {
            2: [4, 6, 8],
            3: [9],
            4: [8],
        }
        downgrades = [0] * 4
        j = i + 2
        c = 0
        while j > 0:
            j -= 1
            if overflow:
                for k in range(2, 10):
                    if counter_numbers[k]:
                        # downgrade if possible
                        counter_numbers[k] -= 1
                        for i_new in range(4):
                            while downgrades[i_new] and k % primes[i_new] == 0:
                                downgrades[i_new] -= 1
                                k //= primes[i_new]

                        new_numbers.append(k)
                        break
                continue

            curr_num = int(num[-j])
            c = 0
            
            for k in range(curr_num, 10):
                if counter_numbers[k]:
                    new_numbers.append(k)
                    counter_numbers[k] -= 1
                    overflow = k != curr_num # we overflown
                    break
            else:
                for k in range(2, 10):
                    if counter_numbers[k]:
                        counter_numbers[k] -= 1
                        
                        for x in transform[k]:
                            if x >= curr_num:
                                a = digit_counts[k]
                                b = digit_counts[x]
                                for j in range(4):
                                    downgrades[j] += b - a
                                overflow = x > curr_num
                                new_numbers.append(x)
                                break
                        else:
                            counter_numbers[k] += 1
                            continue
                        break
                else:
                    counter_numbers[1] += 1
                    j += 2
                    c = 1

        
        res = num[:-i - 1] + "".join(map(str, new_numbers))
        return res


if __name__ == "__main__":
    num = "19"
    t = 2
    print(Solution().smallestNumber(num, t))


# 3 hours passed, i hate it, no thanks