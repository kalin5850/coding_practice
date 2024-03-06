def bubble_sort(numbers_list):
    "bubble up the smallest number to the left"
    for i in range(len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] > numbers_list[j]:
                tmp = numbers_list[j]
                numbers_list[j] = numbers_list[i]
                numbers_list[i] = tmp
        print("Thie %sth sorting result %s" % (i, numbers_list))

    return numbers_list


if __name__ == "__main__":
    numbers_list = [5, 9, 3, 10, 45, 2, 0]
    print(bubble_sort(numbers_list=numbers_list))
