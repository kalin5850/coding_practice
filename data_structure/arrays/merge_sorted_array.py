def merge_sorted_array1(arr1, arr2):
    if len(arr1) < len(arr2):
        minimun_length = len(arr1)
        maximun_lenght = len(arr2)
        compare_array1 = arr1.copy()
        compare_array2 = arr2.copy()
    else:
        minimun_length = len(arr2)
        maximun_lenght = len(arr1)
        compare_array1 = arr2.copy()
        compare_array2 = arr1.copy()

    i = 0
    result = []
    while i < minimun_length:
        if i == 0 and compare_array1[i] < compare_array2[i]:
            result.append(compare_array1[i])
            result.append(compare_array2[i])
            i += 1
            continue
        elif i == 0 and compare_array1[i] > compare_array2[i]:
            result.append(compare_array2[i])
            result.append(compare_array1[i])
            i += 1
            continue
        if (
            i > 0
            and compare_array1[i] < compare_array2[i]
            and result[len(result) - 1] < compare_array1[i]
        ):
            result.append(compare_array1[i])
            result.append(compare_array2[i])
            i += 1
            continue
        elif (
            i > 0
            and compare_array1[i] < compare_array2[i]
            and result[len(result) - 1] > compare_array1[i]
        ):
            result.insert(len(result) - 1, compare_array1[i])
            result.append(compare_array2[i])
            i += 1
            continue
        elif (
            i > 0
            and compare_array1[i] > compare_array2[i]
            and result[len(result) - 1] < compare_array2[i]
        ):
            result.append(compare_array2[i])
            result.append(compare_array1[i])
            i += 1
            continue
        elif (
            i > 0
            and compare_array1[i] > compare_array2[i]
            and result[len(result) - 1] > compare_array2[i]
        ):
            result.insert(len(result) - 1, compare_array2[i])
            result.append(compare_array1[i])
            i += 1
            continue

    i = minimun_length
    while i < maximun_lenght:
        if result[len(result) - 1] < compare_array2[i]:
            result.append(compare_array2[i])
        else:
            result.insert(len(result) - 1, compare_array2[i])
        i += 1
    return result


def merge_sorted_array2(arr1, arr2):
    pass


def merge_sorted_array3(arr1, arr2):
    """
    Time Complexity: O(nlogn)
    Auxiliary Space: O(n)
    """
    return sorted(arr1 + arr2)


def merge_sorted_array4(arr1, arr2):
    """
    Time Complexity: O(nlogn)
    Auxiliary Space: O(n)
    """
    import itertools

    return sorted(itertools.chain(arr1, arr2))


if __name__ == "__main__":
    a = [1, 5, 9, 15, 19]
    b = [6, 8, 12, 20, 25, 26]

    print(merge_sorted_array1(a, b))
    print(merge_sorted_array3(a, b))
    print(merge_sorted_array4(a, b))
