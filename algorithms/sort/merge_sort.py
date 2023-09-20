def merge(left, right):
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list
    middle = len(numbers_list) // 2
    left = merge_sort(numbers_list=numbers_list[0:middle])
    right = merge_sort(numbers_list=numbers_list[middle : len(numbers_list)])

    return merge(left=left, right=right)


if __name__ == "__main__":
    numbers_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(merge_sort(numbers_list=numbers_list))
