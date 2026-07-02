global_list = [2, 4, 10, 10]


def sum_list(numbers):
    for element in numbers:
        if not isinstance(element, int):
            raise TypeError("All elements must be numbers")
    return sum(numbers)


print(sum_list(global_list))


if __name__ == '__main__':
    print(sum_list(global_list))