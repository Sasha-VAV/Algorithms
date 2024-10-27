import subprocess


def run_test(test_input, expected_output, test_num):
    process = subprocess.Popen(
        ['python', 'task1C.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=test_input)

    if output.strip() == expected_output.strip():
        print(f"Тест на строке {test_num} пройден!")
    else:
        print(f"Тест на строке {test_num} не пройден.")
        print(f"Ожидалось: {expected_output.strip()}")
        print(f"Получено: {output.strip()}")


if __name__ == "__main__":
    with open('Tests_1.3.txt', 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        N = int(lines[i].strip())
        array = ""
        for j in range(0, N):
            array += lines[i + j + 1].strip() + "\n"
        answer = lines[i + N + 1].strip()

        test_input = f"{N}\n{array}\n{answer}\n"
        expected_output = answer

        run_test(test_input, expected_output, i)
        i += N + 3
