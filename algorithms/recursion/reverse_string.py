def reverse_string(strings):
    if len(strings) == 0:
        return strings
    else:
        return reverse_string(strings[1:]) + strings[0]


if __name__ == "__main__":
    result = []
    print(reverse_string(strings="yoyo mastery"))
