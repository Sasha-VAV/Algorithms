class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        If value divided by 3 - "Fizz",
        value divided by 5 - "Buzz",
        value divided by 15 - "FizzBuzz",
        else - value.
        :param n: size of sequence
        :return: list of values.
        """
        fizz_buzz_list: List[Union[int, str]] = []
        count_3 = 2
        count_5 = 4
        for x in range(1, n + 1):
            if count_3 == 0 and count_5 == 0:
                fizz_buzz_list.append("FizzBuzz")
                count_3 = 3
                count_5 = 5
            elif count_3 == 0:
                fizz_buzz_list.append("Fizz")
                count_3 = 3
            elif count_5 == 0:
                fizz_buzz_list.append("Buzz")
                count_5 = 5
            else:
                fizz_buzz_list.append(str(x))
            count_3 -= 1
            count_5 -= 1
        return fizz_buzz_list