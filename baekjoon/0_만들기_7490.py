import copy


def numerical(arr, n):
    if len(arr) == n:
        numeri.append(copy.deepcopy(arr))
        # print(numeri)
        return

    arr.append(' ')
    numerical(arr, n)
    arr.pop()

    arr.append('+')
    numerical(arr, n)
    arr.pop()

    arr.append('-')
    numerical(arr, n)
    arr.pop()


for _ in range(int(input())):
    n = int(input())

    numeri = []

    n_list = [i+1 for i in range(n)]
    numerical([], n-1)

    # print(strings, numeri)

    for i in numeri:
        res = ''

        for j in range(n - 1):
            res += str(n_list[j]) + i[j]
        res += str(n_list[-1])

        if eval(res.replace(" ", "")) == 0:
            print(res)
    print()


# print(res)
