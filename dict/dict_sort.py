family = {
    'Aleksander': 37,
    'Emmanuel': 3,
    'Bogdan': 1,
    'Irina': 39,
    'Timothy': 15,
    'Michael': 7,
    'Tatyana': 11,
    'Ekaterina': 10,
    'Taisiya': 14
}


# Не моё решение (с изменениями). TODO: доработать
def dict_sort_1(dictionary):
    """ Возвращает новый отсортированный по значениям и ключам словарь. """
    new_dict = {}
    for el in sorted(dictionary.items(), key=lambda pair: (pair[1], pair[0])):
        new_dict[el[0]] = el[1]
    return new_dict


if __name__ == '__main__':
    print(dict_sort_1(family))
    print(family)
