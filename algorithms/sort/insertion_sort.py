def insertion_sort(numbers_list):
    for i in range(len(numbers_list)):
        j = i - 1
        while j >= 0:
            if numbers_list[i] < numbers_list[j]:
                tmp = numbers_list[i]
                numbers_list[i] = numbers_list[j]
                numbers_list[j] = tmp
                j -= 1
                i -= 1
            else:
                break

    return numbers_list


if __name__ == "__main__":
    numbers_list = [5, 9, 3, 10, 45, 2, 0]
    print(insertion_sort(numbers_list=numbers_list))
