def fibonacci_resursion(index):
    "O(2^n)"
    if index < 2:
        return index
    return fibonacci_resursion(index - 1) + fibonacci_resursion(index - 2)


def fibonacci_loop(index):
    "index >= 2"
    base_num_1 = 0
    base_num_2 = 1
    tmp = 0
    for i in range(1, index):
        tmp = base_num_1 + base_num_2
        base_num_1 = base_num_2
        base_num_2 = tmp
    return tmp


if __name__ == "__main__":
    print(fibonacci_resursion(10))
    print(fibonacci_loop(10))
