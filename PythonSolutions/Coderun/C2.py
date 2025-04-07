import sys


def main():
    a, b = map(int, input().split())
    arr = []
    for i in range(a):
        arr.append(list(map(int, input().split())))
    costs = arr
    for i in range(a):
        for j in range(b):
            if i == 0:
                if j == 0:
                    addition = 0
                else:
                    addition = costs[i][j - 1]
            else:
                if j == 0:
                    addition = costs[i - 1][j]
                else:
                    addition = min(costs[i][j - 1], costs[i - 1][j])

            costs[i][j] += addition
    print(costs[a-1][b-1])
    pass


if __name__ == '__main__':
    main()