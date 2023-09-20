def selection_sort(numbers_list):
    "looking for the smallest number and swaping to the front"
    for i in range(len(numbers_list)):
        smallest = numbers_list[i]
        smallest_index = i
        for j in range(i + 1, len(numbers_list)):
            if smallest > numbers_list[j]:
                smallest = numbers_list[j]
                smallest_index = j

        tmp = numbers_list[i]
        numbers_list[i] = numbers_list[smallest_index]
        numbers_list[smallest_index] = tmp

    return numbers_list


if __name__ == "__main__":
    numbers_list = [5, 9, 3, 10, 45, 2, 0]
    print(selection_sort(numbers_list=numbers_list))
