def reverse_string1(strs):
    tmp = ""
    for i in range(len(strs)):
        tmp = tmp + strs[len(strs) - i - 1]
    return tmp


def reverse_list(list1):
    times = len(list1) // 2
    for i in range(times):
        tmp = list1[i]
        list1[i] = list1[len(list1) - i - 1]
        list1[len(list1) - i - 1] = tmp

    return list1


if __name__ == "__main__":
    list1 = ["a", "b", "c", "d", "e"]
    strs = "a b c d e"
    print(reverse_string1(strs))
    print(reverse_list(list1))
