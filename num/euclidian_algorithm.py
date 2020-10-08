# В некторых случаях долгий
def euclidian_algorithm_heavy(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# Более быстрый и лёгкий
def euclidian_algorithm(a, b):
    while b > 0:
        # c = a % b
        # a = b
        # b = c
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print(euclidian_algorithm(49, 58))
    print(euclidian_algorithm(1024, 999))
    print(euclidian_algorithm(128, 45))
    print(euclidian_algorithm(533, 528))
    print(euclidian_algorithm(35, 45))
    print(euclidian_algorithm(999, 333))
    print(euclidian_algorithm(999, 888))
    print(euclidian_algorithm(999, 45))
