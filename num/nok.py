from euclidian_algorithm import euclidian_algorithm as nod


def nok(a, b):
    n = (a * b) / nod(a, b)
    return int(n)


if __name__ == '__main__':
    print(nok(80, 16))
    print(nok(111, 8))
    print(nok(112, 32))
    print(nok(999, 333))
    print(nok(999, 888))
    print(nok(999, 45))
