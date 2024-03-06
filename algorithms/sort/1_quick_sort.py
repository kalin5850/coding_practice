def partition1(numbers_list, start, end):
    pivot = numbers_list[start]
    low = start + 1
    high = end
    while low < high:
        while numbers_list[low] < pivot:
            low += 1
            # continue
        while numbers_list[high] > pivot:
            high -= 1
            # continue
        if low < high:
            tmp = numbers_list[low]
            numbers_list[low] = numbers_list[high]
            numbers_list[high] = tmp

    if pivot > numbers_list[high]:
        numbers_list[start] = numbers_list[high]
        numbers_list[high] = pivot
    return high


def quick_sort(numbers_list, start, end):
    if end <= start:
        return numbers_list
    pivot_index = partition1(numbers_list=numbers_list, start=start, end=end)
    quick_sort(numbers_list, start, pivot_index - 1)
    quick_sort(numbers_list, pivot_index + 1, end)

    return numbers_list


if __name__ == "__main__":
    numbers_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4]
    # numbers_list = [0, 1, 2, 3]
    print(quick_sort(numbers_list=numbers_list, start=0, end=len(numbers_list) - 1))
