def all_dividers(num):
    i = 1
    a = []
    while i ** 2 <= num:
        if num % i == 0:
            a.append(i)
            if i != num // i:
                a.append(num // i)
        i += 1
    a.sort()
    return a


if __name__ == '__main__':
    print(all_dividers(25))
    print(all_dividers(36))
    print(all_dividers(999))
    print(all_dividers(128))
    print(all_dividers(1024))
